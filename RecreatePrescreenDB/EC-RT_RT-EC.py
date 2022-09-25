import json
from loguru import logger

def Traverse():
    with open(".\\EC-RT.json", "r") as ifp:
        EC_RTJson = json.load(ifp)
    RT_EC_Dic = {}
    for ec_num in EC_RTJson:
        for rt in EC_RTJson[ec_num]:
            if rt not in RT_EC_Dic:
                RT_EC_Dic[rt] = [ec_num]
            else:
                RT_EC_Dic[rt].append(ec_num)
        logger.success(f"{ec_num} successfully parsed.")
    with open(".\\RT_EC.json", "w") as ofp:
        json.dump(RT_EC_Dic, ofp, ensure_ascii=False, indent=4)

Traverse()
