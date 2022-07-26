# 用于计算化学反应的相似度
import os
os.environ['R_HOME'] = 'D:\\R\\R-4.2.1'
os.environ['R_USER'] = 'D:\\Applications\\Anaconda\\envs\\igem\\Lib\\site-packages\\rpy2'
from rpy2 import robjects
from rpy2.robjects.packages import importr
import time
import threading


class CustomTask:
    def __init__(self):
        self._result = {}

    def run(self, lis, start, end, user_reaction):
        importr("RxnSim")
        enz_dic = {}
        for i in range(start, end + 1):
            ec_num = lis[i][0]
            reaction = lis[i][1]
            if 'exception' in reaction:
                continue
            dic = {}
            sim = robjects.r['rs.compute'](reaction, user_reaction)
            if ec_num not in enz_dic:
                dic['similarity'] = sim[0]
                dic['most_similarity_reaction'] = reaction
                enz_dic[ec_num] = dic
            else:
                if enz_dic[ec_num]['similarity'] < sim[0]:
                    enz_dic[ec_num]['similarity'] = sim[0]
                    enz_dic[ec_num]['most_similar_reaction'] = reaction
        self._result = enz_dic

    def get_result(self):
        return self._result


def CopeEnz(enz_list, user_reaction):
    t1 = time.process_time()
    # enz_list 中的元素是 Enzyme 对象
    # user_reaction 是用户给出的化学反应
    enz_lis_len = len(enz_list)
    seg = int(enz_lis_len / 2)
    ct1 = CustomTask()
    th1 = threading.Thread(target=ct1.run, args=(enz_list, 0, seg, user_reaction))
    ct2 = CustomTask()
    th2 = threading.Thread(target=ct2.run, args=(enz_list, seg+1, enz_lis_len-1, user_reaction))
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    results = []
    results.append(ct1.get_result())
    results.append(ct2.get_result())
    # print(results)

    enz_dic = {}  # 该字典以酶的 ec 编码为键，以和酶有关的信息（类型为字典）为值
    for i in range(2):
        dic = {}
        for ec_num in results[i]:
            if ec_num not in enz_dic:
                dic['similarity'] = results[i][ec_num]['similarity']
                dic['most_similar_reaction'] = results[i][ec_num]['most_similar_reaction']
                enz_dic[ec_num] = dic
            else:
                if enz_dic[ec_num]['similarity'] < results[i][ec_num]['similarity']:
                    enz_dic[ec_num]['similarity'] = results[i][ec_num]['similarity']
                enz_dic[ec_num]['most_similar_reaction'] = results[i][ec_num]['most_similar_reaction']

    # 接下来要给 enz_dic 按值的内容进行排序

    # 按相似度进行排序，并按降序输出
    lis = sorted(enz_dic, key=lambda k: enz_dic[k]['similarity'], reverse=True)

    final_enz_dic = {}
    for ec in lis[:5]:  # 取前 30 种酶
        final_enz_dic[ec] = enz_dic[ec]
    t2 = time.process_time()
    final_enz_dic['time'] = t2 - t1
    final_enz_dic['len'] = len(enz_list)
    return final_enz_dic  # 这个字典可以直接用 json.dumps 转化成 JSON 字符串


# if __name__ == '__main__':
#
#     rxnsim = importr('RxnSim')
#     t = robjects.r['ms.compute']('CO', 'CCO')
#     print(t[0])
