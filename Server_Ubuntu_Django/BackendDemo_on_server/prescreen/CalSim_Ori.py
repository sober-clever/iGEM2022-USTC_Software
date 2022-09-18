# 用于计算化学反应的相似度
import os
os.environ['R_HOME'] = 'D:\\R\\R-4.2.1'
os.environ['R_USER'] = 'D:\\Applications\\Anaconda\\envs\\igem\\Lib\\site-packages\\rpy2'
from rpy2 import robjects
from rpy2.robjects.packages import importr
import time


def CopeEnz(enz_list, user_reaction):
    t1 = time.process_time()
    # enz_list 中的元素是 Enzyme 对象
    # user_reaction 是用户给出的化学反应
    rxnsim = importr('RxnSim')
    enz_dic = {}  # 该字典以酶的 ec 编码为键，以和酶有关的信息（类型为字典）为值
    for enz_lis in enz_list:
        ec_num = enz_lis[0]
        reaction = enz_lis[1]
        if 'exception' in reaction:
            continue
        most_sim_reaction = ''  # 用于记录与用户给出的反应最像的反应
        dic = {}
        # 循环用于计算 该酶被筛选出的所有反应 中与 用户给出的反应 的相似度的最大值
        sim = robjects.r['rs.compute'](reaction, user_reaction)
        if ec_num not in enz_dic:
            dic['similarity'] = sim[0]
            dic['most_similar_reaction'] = reaction
            enz_dic[ec_num] = dic
        else:
            if enz_dic[ec_num]['similarity'] < sim[0]:
                enz_dic[ec_num]['similarity'] = sim[0]
                enz_dic[ec_num]['most_similar_reaction'] = reaction

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
