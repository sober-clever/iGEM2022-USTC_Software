from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Query, Query2, Redox, Mustcontain, Elimination, Ismerization, \
    Hydrolysis, Transfer, Ligation, Enzyme, Reaction, Organism, Kinetic, Phtemp, Km, Kcat_Km
from .serializers import QuerySerializer, Query2Serializer
from rdkit import Chem
# from .CalSim_Ori import CopeEnz
# import socket
import json
import rpyc
import time
from itertools import combinations
# 用于定义请求响应的逻辑


@api_view(['GET'])
def article_list(request):
    # articles = Article.objects.all()
    # serializer = ArticleListSerializer(articles, many=True)
    # return JsonResponse(serializer.data, safe=False)
    if request.method == 'GET':
        import random
        num_dic = {}
        for i in range(30):
            dic = {}
            dic['aa'] = random.randint(0, 100)
            dic['bb'] = random.random()
            num_dic[i] = dic

        lis = sorted(num_dic, key=lambda k: num_dic[k]['bb'], reverse=True)

        new_dic = {}
        for i in lis[:5]:
            new_dic[i] = num_dic[i]

        import json
        # print(new_dic)
        # print(json.dumps(new_dic))
        return Response(json.dumps(new_dic))


def get_soundex(string: str):
    with connection.cursor() as cursor:
        cursor.execute("SELECT SOUNDEX(%s)", (string,))
        return cursor.fetchone()[0]


@api_view(['GET', 'POST'])
def query_list(request):    # 用于根据给出的反应查询酶的信息
    if request.method == "GET":
        queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # return Response(request.data)
        t1 = time.time()
        # dic = json.loads(request.data)
        serializer = QuerySerializer(data=request.data)
        # serializer = QuerySerializer(data=dic)
        # return Response(request.data)
        if serializer.is_valid():
            # return Response(request.data)
            serializer.save()
            dic = request.data
            # product = request.data['product']
            MustQueryset = Mustcontain.objects.all()
            FirstQueryset = MustQueryset
            if dic["type"]:  # if-else 懒得写
                if dic["type"] == 1:
                    ChoiceQueryset = Redox.objects.all()
                elif dic["type"] == 2:
                    ChoiceQueryset = Transfer.objects.all()
                elif dic["type"] == 3:
                    ChoiceQueryset = Hydrolysis.objects.all()
                elif dic["type"] == 4:
                    ChoiceQueryset = Elimination.objects.all()
                elif dic["type"] == 5:
                    ChoiceQueryset = Ismerization.objects.all()
                    from django.db import connection
                else:
                    ChoiceQueryset = Ligation.objects.all()
                FirstQueryset = FirstQueryset.union(ChoiceQueryset)
                # FirstQueryset = FirstQueryset.union(Elimination.objects.all())
                # FirstQueryset = FirstQueryset.union(Decarboxylation.objects.all())
                # FirstQueryset = FirstQueryset.union(Transfer.objects.all())
                # FirstQueryset = FirstQueryset.union(Hydrolysis.objects.all())
                # FirstQueryset = FirstQueryset.union(Others.objects.all())

                FirstList = []
                for i in FirstQueryset:
                    FirstList.append(i.ec_num)
                SecondQueryset = Reaction.objects \
                    .filter(ec_num__in=FirstList) \
                    # .filter(substrate__contains=dic["reactant"]["reactionAtoms"][0]) \
                # .filter(product__contains=dic["product"]["reactionAtoms"][0])
                PrescreenResult = []
                # for i in SecondQueryset:
                #     PrescreenResult.append([i.ec_num, i.reaction])

                sub = dic['reactant']['smiles']
                # sub_atom_num = dic['reactant']['partflag']  # 参与反应的原子总数
                sub_lis = dic['reactant']['reactionAtoms']  # 参与反应的原子列表
                sub_len = len(sub_lis)

                sub_mol = Chem.MolFromSmiles(sub)   # mol 格式的反应物
                sub_bonds = []
                sub_atom_path = [sub_lis[str(i)][1] for i in range(sub_len)]
                have_neighbor = []
                for i, j in combinations(sub_atom_path, 2):
                    b = sub_mol.GetBondBetweenAtoms(i, j)
                    if b:
                        have_neighbor.append(i)
                        have_neighbor.append(j)
                        sub_bonds.append(b.GetIdx())
                sub_substruct = Chem.PathToSubmol(sub_mol, sub_bonds)
                # 反应物指定的基团
                sub_isolate_atom = [sub_lis[str(i)][0] for i in range(sub_len) if
                                    sub_lis[str(i)][1] not in have_neighbor]
                # 反应物指定的原子中孤立的部分

                pro = dic['product']['smiles']
                pro_atom_num = dic['product']['partflag']
                pro_lis = dic['product']['reactionAtoms']
                pro_len = len(pro_lis)

                pro_mol = Chem.MolFromSmiles(pro)
                pro_bonds = []
                pro_atom_path = [pro_lis[str(i)][1] for i in range(pro_len)]
                have_neighbor = []
                for i, j in combinations(pro_atom_path, 2):
                    b = pro_mol.GetBondBetweenAtoms(i, j)
                    if b:
                        have_neighbor.append(i)
                        have_neighbor.append(j)
                        pro_bonds.append(b.GetIdx())
                pro_substruct = Chem.PathToSubmol(pro_mol, pro_bonds)
                # 生成物指定的子结构中连在一起的部分

                pro_isolate_atom = [pro_lis[str(i)][0] for i in range(pro_len) if
                                    pro_lis[str(i)][1] not in have_neighbor]
                # 生成物指定的子结构中孤立的部分

                required_cofactor = dic["cofactors"]

                cnt = 0
                req_orga = dic["organism"]  # abbr. for required_organism 获得种属信息（用户未填则为空）
                OrganismQueryset = Organism.objects.filter(organism=req_orga)
                req_orga_ecs = []
                for elm in OrganismQueryset:
                    req_orga_ecs.append(elm.ec_num)
                # test_lis = []
                for elm in SecondQueryset:
                    # if elm.reaction in test_lis:
                    #     continue

                    if req_orga != "" and elm.ec_num not in req_orga_ecs:   # 酶对应的种属需要满足用户要求的种属
                        continue

                    if required_cofactor != [] and not elm.cofactor:
                        continue

                    lis = elm.cofactor.split(" ")
                    # print(lis)
                    flag = False
                    for co in lis:
                        if co in required_cofactor:
                            flag = True  # 说明辅因子符合要求
                    if required_cofactor != [] and flag is False:  # 该酶的辅因子不符合要求
                        continue

                    substrate = Chem.MolFromSmiles(elm.substrate)
                    product = Chem.MolFromSmiles(elm.product)
                    if not substrate or not product:
                        cnt = cnt + 1
                        continue
                    # result.append(elm.substrate)
                    sub_matches = substrate.GetSubstructMatches(sub_substruct)
                    pro_matches = product.GetSubstructMatches(pro_substruct)
                    if Chem.MolToSmiles(sub_substruct) != "" and sub_matches == ():
                        continue
                    if Chem.MolToSmiles(pro_substruct) != "" and pro_matches == ():
                        continue
                    sub_isolate_atom_str = '.'.join(sub_isolate_atom)
                    pro_isolate_atom_str = '.'.join(pro_isolate_atom)
                    sub_matches2 = substrate.GetSubstructMatches(Chem.MolFromSmiles(sub_isolate_atom_str))
                    pro_matches2 = product.GetSubstructMatches(Chem.MolFromSmiles(pro_isolate_atom_str))
                    if pro_isolate_atom != [] and pro_matches2 == ():
                        continue
                    if sub_isolate_atom != [] and sub_matches2 == ():
                        continue
                    # test_lis.append(elm.reaction)
                    PrescreenResult.append([elm.ec_num, elm.reaction, elm.cofactor])

                t2 = time.time()

                user_reaction = dic['reactant']['smiles'] + '>>' + dic['product']['smiles']
                # ret_val = CopeEnz(PrescreenResult, user_reaction)
                conf = rpyc.core.protocol.DEFAULT_CONFIG
                conf['allow_pickle'] = True
                conf['sync_request_timeout'] = None
                conn = rpyc.connect('118.195.163.237', port=9998, config=conf)
                ret_val = conn.root.get_enz_dic(PrescreenResult, user_reaction)
                # ret_json = json.dumps(ret_val)
                # ret_val = {}
                # ret_val['str'] = conn.root.get_time()
                t3 = time.time()
                conn.close()
                # ret_val = dict(ret_val)
                # 通过该种方式可以提取 product
            # 通过 product['smiles'] 访问 smiles 属性
            # 通过 product['reactionAtoms']['0'][0] 和 通过 product['reactionAtoms']['0'][1]
            # 可以访问产物被指定基团的内容和它在 smiles 字符串中的位置
            # 从而可以将输入正确地转化成需要的数据
            # return Response(product['reactionAtoms']['0'][1], status=status.HTTP_200_OK)
                dic_ = json.loads(ret_val)
                # dic_ = {}
                # dic_['type'] = type(ret_val)
                # dic_['string'] = ret_val
                # dic_['content'] = ret_val
                req_soundex = get_soundex(req_orga)
                EnzymeQuerySet = Enzyme.objects.filter(ec_num__in=dic_['ecs'])
                KinQueryset1 = Phtemp.objects.filter(soundex=req_soundex)
                Kcat_KmQueryset1 = Kcat_Km.objects.filter(soundex=req_soundex)
                KmQueryset1 = Km.objects.filter(soundex=req_soundex)
                for enzyme in EnzymeQuerySet:
                    dic_[enzyme.ec_num]['name'] = enzyme.ec_name

                    dic_[enzyme.ec_num]['kinetic'] = []

                    if req_orga != "":  # 动力学常数需要事先给出种属
                        KinQueryset = KinQueryset1.filter(ec_num=enzyme.ec_num)
                        for elm in KinQueryset:
                            refrence_link = "https://www.brenda-enzymes.org/literature.php?e=" + elm.ec_num \
                                            +"&r="+elm.literture
                            dic_[enzyme.ec_num]['kinetic'].append([elm.ph, elm.temp, refrence_link])

                        dic_[enzyme.ec_num]['substrate_info'] = []
                        if dic_[enzyme.ec_num]['cofactor'] in ["NADH", "NADPH"]:
                            Kcat_KmQueryset = Kcat_KmQueryset1.filter(ec_num=enzyme.ec_num)
                            # KmQueryset = KmQueryset1.filter(substrate__in=kcat_km_sub_info)filter(ec_num=enzyme.ec_num)
                            kcat_km_sub_info = []
                            for kcat_km in Kcat_KmQueryset:
                                if kcat_km not in kcat_km_sub_info:
                                    kcat_km_sub_info.append(kcat_km.substrate)
                            KmQueryset = KmQueryset1.filter(substrate__in=kcat_km_sub_info).filter(ec_num=enzyme.ec_num)
                            # km_sub_info = []
                            for km in KmQueryset:
                                if km.substrate not in dic_[enzyme.ec_num]['substrate_info']:
                                    # km_sub_info.append(km.substrate)
                                    dic_[enzyme.ec_num]['substrate_info'].append(km.substrate)
                            # for elm in kcat_km_sub_info:
                            #     if elm in km_sub_info and elm not in dic_[enzyme.ec_num]['substrate_info']:

                # for elm in dic_['ecs']:
                #     ReactionQuerySet = Reaction.objects.filter(ec_num=elm).filter(reaction=dic_[elm]\
                #         ['most_similar_reaction'])
                #     dic_[elm]['cofactor'] = ReactionQuerySet[0].cofactor

                dic_['primary_selection_time'] = t2 - t1  # 初筛所需的时间
                dic_['compare_time'] = t3 - t2  # 比对所需时间
                dic_['compare_len'] = len(PrescreenResult)  # 比对的长度
            #     dic = {}
            #     dic['type'] = type(ret_val)
            #     dic['content'] = ret_val
            return Response(json.dumps(dic_), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def fun(ec, sub, ogsm, temp, ph, cofactor):

    if cofactor == "NADH":
        sub2 = "NAD+"
    elif cofactor == "NADPH":
        sub2 = "NADP+"

    KmQueryset1 = Km.objects.filter(ec_num=ec).filter(substrate=sub). \
        filter(speciesname=ogsm)

    Kcat_KmQueryset1 = Kcat_Km.objects.filter(ec_num=ec).filter(substrate=sub). \
        filter(speciesname=ogsm)

    KmQueryset2 = Km.objects.filter(ec_num="1.1.1.47").filter(substrate=sub2). \
        filter(speciesname=ogsm)

    Kcat_KmQueryset2 = Kcat_Km.objects.filter(ec_num="1.1.1.47").filter(substrate=sub2). \
        filter(speciesname=ogsm)

    if temp != "":
        temp = float(temp)
        temp_low = temp - 10
        temp_high = temp + 10
        KmQueryset1 = KmQueryset1.filter(temp__range=(temp_low, temp_high))
        Kcat_KmQueryset1 = Kcat_KmQueryset1.filter(temp__range=(temp_low, temp_high))
        KmQueryset2 = KmQueryset2.filter(temp__range=(temp_low, temp_high))
        Kcat_KmQueryset2 = Kcat_KmQueryset2.filter(temp__range=(temp_low, temp_high))

    if ph != "":
        ph = float(ph)
        ph_low = ph - 2
        ph_high = ph + 2
        KmQueryset1 = KmQueryset1.filter(ph__range=(ph_low, ph_high))
        Kcat_KmQueryset1 = Kcat_KmQueryset1.filter(ph__range=(ph_low, ph_high))
        KmQueryset2 = KmQueryset2.filter(ph__range=(ph_low, ph_high))
        Kcat_KmQueryset2 = Kcat_KmQueryset2.filter(ph__range=(ph_low, ph_high))


    km_min1, km_max1 = 1e5, 0
    kcatkm_min1, kcatkm_max1 = 1e5, 0
    km_min2, km_max2 = 1e5, 0
    kcatkm_min2, kcatkm_max2 = 1e5, 0
    for km in KmQueryset1:
        km_min1, km_max1 = min(km_min1, km.km), max(km_max1, km.km)
    for kcatkm in Kcat_KmQueryset1:
        kcatkm_min1, kcatkm_max1 = min(kcatkm_min1, kcatkm.kcat_km), max(kcatkm_max1, kcatkm.kcat_km)
    for km in KmQueryset2:
        km_min2, km_max2 = min(km_min2, km.km), max(km_max2, km.km)
    for kcatkm in Kcat_KmQueryset2:
        kcatkm_min2, kcatkm_max2 = min(kcatkm_min2, kcatkm.kcat_km), max(kcatkm_max2, kcatkm.kcat_km)
    # 返回的两个值可能相等，表示只有一个值，无需区间表示
    return (km_min1, km_max1), (kcatkm_min1, kcatkm_max1), (km_min2, km_max2), (kcatkm_min2, kcatkm_max2)


@api_view(['GET', 'POST'])
def sencond_query(request):
    if request.method == "GET":
        queries = Query2.objects.all()
        serializer = Query2Serializer(queries, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = Query2Serializer(data=request.data)
        if serializer.is_valid():
            dic = request.data
            # ph 和 temp 可能为空串
            ph = dic['ph']
            temp = dic['temp']
            substrate_info = dic['substrate_info']
            ec_num = dic['ec_num']
            organism = dic['organism']
            cofactor = dic['cofactor2']
            km1_range, kcat1_range, km2_range, kcat2_range = fun(ec_num, substrate_info, organism, temp, ph, cofactor)
            dic_ = {}
            dic_['km1_range'] = km1_range
            dic_['kcat1_range'] = kcat1_range
            dic_['km2_range'] = km2_range
            dic_['kcat2_range'] = kcat2_range
            return Response(json.dumps(dic_), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# primary api for test
# def prescreen(request):
#     if request.method == "GET":
#         return render(request, 'prescreen.html')
#     if request.method == "POST":
#         RequestDict = json.loads(request.data)
#         MustQueryset = Mustcontain.objects.__all__()
#         if RequestDict["Choice"]:  # if-else 懒得写
#             ChoiceQueryset = Redox.objects.__all__()
#             FirstQueryset = MustQueryset.union(MustQueryset, ChoiceQueryset)
#             FirstList = []
#             for i in FirstQueryset:
#                 FirstList.append(i.ec_num)
#             SecondQueryset = Reaction.objects \
#                 .filter(ec_num__in=FirstList) \
#                 .filter(substrate__contains=RequestDict["substrate_group"]) \
#                 .filter(product__contains=RequestDict["product_group"])
#             PrescreenResult = []
#             for i in SecondQueryset:
#                 PrescreenResult.append([i.ec_num, i.reaction])
#             # Return PrescreenResult
#


