import json
from loguru import logger

def Traverse():
    with open(".\\brenda_download.txt", "r") as ifp:
        with open(".\\220925\\EC-RT.json", "w") as ofp:
            line = ifp.readline()
            dic = {}
            ID = 0
            while 1:
                if line == "":
                    break
                # Operation Start
                if "///" in line:   # Next line is "ID xxx"
                    line = ifp.readline()
                    lineList = line.split("\t")
                    try:
                        ID = lineList[1].replace("\n", "")
                        dic[ID] = []
                        continue
                    except:
                        logger.error(f"ID error:{line}")
                        continue
                elif "REACTION_TYPE" in line: # Next few lines are "RT xxx"
                    line = ifp.readline()
                    while 1:
                        if "RT" not in line:
                            logger.success(f"{ID} successfully parsed.")
                            break
                        lineList = line.split("\t")
                        reaction_type = lineList[1].replace("\n", "")
                        if "(" in reaction_type:
                            reaction_type = reaction_type.split("(")[0]
                            if reaction_type[-1] == ' ':
                                reaction_type = reaction_type[:-1]
                            while 1:
                                line = ifp.readline()
                                if "///" in line or "RT" in line or line == "":
                                    break
                        # Optimization to simplify RTList
                        if "hydrolysis of" in reaction_type:
                            reaction_type = "hydrolysis"
                        #
                        dic[ID].append(reaction_type)
                        line = ifp.readline()
                else:
                    line = ifp.readline()
                # Operation End
            json.dump(dic, ofp, ensure_ascii=False, indent=4)
    return

Traverse()
