from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from testapp.models import Article, Query, Compound
from testapp.serializers import ArticleListSerializer, QuerySerializer
import json


# Create your views here.
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


@api_view(['GET', 'POST'])
def query_list(request):
    if request.method == "GET":
        queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            product = request.data['product']

            # 通过该种方式可以提取 product
            # 通过 product['smiles'] 访问 smiles 属性
            # 通过 product['reactionAtoms']['0'][0] 和 通过 product['reactionAtoms']['0'][1]
            # 可以访问产物被指定基团的内容和它在 smiles 字符串中的位置
            # 从而可以将输入正确地转化成需要的数据
            return Response(product['reactionAtoms']['0'][1], status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
