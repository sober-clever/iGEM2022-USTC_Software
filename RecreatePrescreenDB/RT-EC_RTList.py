import json
from loguru import logger

def Traverse():
    with open(".\\RT_EC.json", "r") as ifp:
        RTECJson = json.load(ifp)
    with open(".\\RTList.txt", "w", encoding="utf-8") as ofp:
        for RT in RTECJson:
            num = len(RTECJson[RT])
            ofp.write(f"{RT}: {num}\n")
    return

Traverse()
