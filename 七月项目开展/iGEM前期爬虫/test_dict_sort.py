import random
num_dic = {}
for i in range(30):
    dic = {}
    dic ['aa'] = random.randint(0,100)
    dic ['bb'] = random.random()
    num_dic[i] = dic

lis = sorted(num_dic, key=lambda k:num_dic[k]['bb'], reverse=True)

new_dic = {}
for i in lis[:5]:
    new_dic[i] = num_dic[i]

import json
print(new_dic)
print(json.dumps(new_dic))