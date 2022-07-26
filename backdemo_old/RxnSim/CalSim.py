# 用于计算化学反应的相似度
from rpy2 import robjects
from rpy2.robjects.packages import importr


class Enzyme:
    # 该类有两个属性，ec 为该酶的 ec 编码， react_list 为筛选出来的该酶能催化的反应
    def __init__(self, ec, reaction_list):
        self.ec = ec
        self.reaction_list = reaction_list


def CopeEnz(enz_list, user_reaction):
    # enz_list 中的元素是 Enzyme 对象
    # user_reaction 是用户给出的化学反应
    rxnsim = importr('RxnSim')
    enz_dic = {}  # 该字典以酶的 ec 编码为键，以和酶有关的信息（类型为字典）为值
    for enz in enz_list:
        temp = 0
        most_sim_reaction = ''  # 用于记录与用户给出的反应最像的反应
        dic = {}
        # 循环用于计算 该酶被筛选出的所有反应 中与 用户给出的反应 的相似度的最大值
        for reaction in enz.reaction_list:
            sim = robjects.r['ms.compute'](reaction, user_reaction)
            if temp < sim[0]:
                temp = sim[0]
                most_sim_reaction = reaction

        dic['similarity'] = temp
        dic['most_similar_reaction'] = most_sim_reaction
        # TODO 后面需要在 dic 中加入 dic['link']，以存储这种酶在 brenda 数据库中的链接
        enz_dic[enz.ec] = dic

    # 接下来要给 enz_dic 按值的内容进行排序

    # 按相似度进行排序，并按降序输出
    lis = sorted(enz_dic, key=lambda k: enz_dic[k]['similarity'], reverse=True)

    final_enz_dic = {}
    for ec in lis[:30]:  # 取前 30 种酶
        final_enz_dic[ec] = enz_dic[ec]
    return final_enz_dic  # 这个字典可以直接用 json.dumps 转化成 JSON 字符串
