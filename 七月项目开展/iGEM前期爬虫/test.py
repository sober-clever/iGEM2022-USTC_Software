import json
s = '{"product":{"entiretyflag":true,"partflag":2,"smiles":"COCC(=O)C1SSCC(N)CC2=CC=CC=C2C1","reactionAtoms":{"0":["S",10],"1":["S",11]}},"reactant":{"entiretyflag":true,"partflag":2,"smiles":"COCC(=O)C(S)CC1=CC=CC=C1CC(N)CS","reactionAtoms":{"0":["S",10],"1":["S",30]}},"type":3}'
dic = json.loads(s)
print(dic)
print(type(dic))

# dic['product']['smiles'] 表示生成物的 smiles
# dic['product']['reactionAtom'] 表示生成物物发生反应的原子

# 反应物同理（把 product 换成 reactant 即可）
# dic['type'] 表示反应类型

# 注意发生反应的原子要注意连的键数以确定该原子是否携带氢
# () 内和边上的原子连一个键，字符串中间的原子连两个键，= 为双键，@ 为叁键，1 表示成环