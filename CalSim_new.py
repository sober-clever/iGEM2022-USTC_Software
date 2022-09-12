# 用于计算化学反应的相似度
import os
# os.environ['R_HOME'] = 'D:\\R\\R-4.2.1'
# os.environ['R_USER'] = 'D:\\Applications\\Anaconda\\envs\\igem\\Lib\\site-packages\\rpy2'
from rpy2 import robjects
from rpy2.robjects.packages import importr
import time
import ray
from rpyc import Service
from rpyc.utils.server import ThreadedServer
import rpyc
import json
# import rpy2.rinterface as ri


@ray.remote# (num_cpus=8, num_gpus=1)
class Worker(object):
    def CalSim(self, lis, start, end, user_reaction):
        importr("RxnSim")
        # ri.embedded._C_stack_limit = None
        # importr("compiler")
        # robjects.r['enableJIT'](1)
        enz_dic = {}
        total_time = 0
        # for i in range(start, end + 1):
        for elm_ in lis[start:end+1] :
            ec_num = elm_[0]
            reaction = elm_[1]
            if 'exception' in reaction:
                continue
            try:
                # coder = 'rs.compute(%s, %s, fpCached=True, algo=\'rsim2\')'%(reaction, user_reaction)
                t1 = time.time()
                param = {'fpCached':True, 'algo':'rsim', 'fp.type':'standard', 'fp.size':1024}
                sim = robjects.r['rs.compute'](reaction, user_reaction, **param)# , fpCached=True, algo='rsim2')
                
                
                # sim = robjects.r('rs.comput(%s,%s)'%(reaction, user_reaction))
                dic = {}
                if ec_num not in enz_dic:
                    dic['similarity'] = sim[0]
                    dic['most_similar_reaction'] = reaction
                    enz_dic[ec_num] = dic
                else:
                    if enz_dic[ec_num]['similarity'] < sim[0]:
                        enz_dic[ec_num]['similarity'] = sim[0]
                        enz_dic[ec_num]['most_similar_reaction'] = reaction
                t2 = time.time()
                total_time += (t2-t1)
            except:
                continue
        enz_dic['rxnsim_time'] = total_time
        return enz_dic


class EnzService(Service):
    def exposed_get_enz_dic(self, enz_list, user_reaction):
        ray.shutdown()
        t1 = time.time()
        ray.init(address='auto')
        # t1 = time.time()
        # enz_list 中的元素是 Enzyme 对象
        # user_reaction 是用户给出的化学反应
        # rxnsim = importr('RxnSim')
        enz_lis_len = len(enz_list)
        # enz_lis_len = 4
        n = 4
        seg = int(enz_lis_len / n)
        futures = []
        # t0 = time.time()
        for i in range(n):
            worker = Worker.remote()
            if i == n - 1:
                end = enz_lis_len - 1
            else:
                end = seg * (i + 1) - 1
            future = worker.CalSim.remote(enz_list, seg * i, end, user_reaction)
            futures.append(future)
        # t00 = time.time()
        t0 = time.time()
        results = ray.get(futures)
        t00 = time.time()
        enz_dic = {}  # 该字典以酶的 ec 编码为键，以和酶有关的信息（类型为字典）为值
        # t0 = time.time()
        for i in range(n):
            for ec_num in results[i]:
                if ec_num == 'rxnsim_time':
                    continue
                if ec_num not in enz_dic:
                    dic = {}
                    dic['similarity'] = results[i][ec_num]['similarity']
                    dic['most_similar_reaction'] = results[i][ec_num]['most_similar_reaction']
                    enz_dic[ec_num] = dic
                else:
                    if enz_dic[ec_num]['similarity'] < results[i][ec_num]['similarity']:
                        enz_dic[ec_num]['similarity'] = results[i][ec_num]['similarity']
                        enz_dic[ec_num]['most_similar_reaction'] = results[i][ec_num]['most_similar_reaction']
        # t00 = time.time()
        # for enz_lis in enz_list:
        #     ec_num = enz_lis[0]
        #     reaction = enz_lis[1]
        #     if 'exception' in reaction:
        #         continue
        #     most_sim_reaction = ''  # 用于记录与用户给出的反应最像的反应
        #     dic = {}
        #     # 循环用于计算 该酶被筛选出的所有反应 中与 用户给出的反应 的相似度的最大值
        #     sim = robjects.r['rs.compute'](reaction, user_reaction)
        #     if ec_num not in enz_dic:
        #         dic['similarity'] = sim[0]
        #         dic['most_similar_reaction'] = reaction
        #         enz_dic[ec_num] = dic
        #     else:
        #         if enz_dic[ec_num]['similarity'] < sim[0]:
        #             enz_dic[ec_num]['similarity'] = sim[0]
        #             enz_dic[ec_num]['most_similar_reaction'] = reaction

        # 接下来要给 enz_dic 按值的内容进行排序

        # 按相似度进行排序，并按降序输出
        # t3 = time.time()
        # t00 = time.time()
        lis = sorted(enz_dic, key=lambda k: enz_dic[k]['similarity'], reverse=True)
        # t4 = time.time()
        final_enz_dic = {}
        ecs = []
        for ec in lis[:30]:  # 取前 30 种酶
            dic_ = {}
            dic_ = enz_dic[ec]
            ecs.append(ec)
            dic_['link'] = 'https://www.brenda-enzymes.org/enzyme.php?ecno=' + ec
            final_enz_dic[ec] = dic_
            # final_enz_dic[ec] = enz_dic[ec]
        t2 = time.time()
        final_enz_dic['ecs'] = ecs
        final_enz_dic['time'] = t2 - t1
        final_enz_dic['len'] = len(enz_list)
        print(final_enz_dic)
        # final_enz_dic['sort_time'] = t4-t3;
        final_enz_dic['rxnsim_time'] = [elm['rxnsim_time'] for elm in results]
        # final_enz_dic['other_time'] = t00 - t0
        return json.dumps(final_enz_dic)  # 这个字典可以直接用 json.dumps 转化成 JSON 字符串


if __name__ == '__main__':
    conf = rpyc.core.protocol.DEFAULT_CONFIG
    conf['allow_pickle'] = True
    conf['sync_request_timeout'] = None
    s = ThreadedServer(service=EnzService, port=9998, auto_register=False, protocol_config=conf)

    s.start()
    # rxnsim = importr('RxnSim')
    # t = robjects.r['ms.compute']('CO', 'CCO')
    # dic = CopeEnz([('1.1.1.1', 'CO>>CCO')],'CCO>>CO')
    # print(dic)
    # print(t[0])




