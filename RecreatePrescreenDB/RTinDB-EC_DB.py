from loguru import logger
import json

@logger.catch
def main():
    with open(".\\RT_EC.json", "r") as f:
        RTECJson = json.load(f)
    spaceErrorRow = []
    FinalRT = {#"Oxidoreductases": [],\
            #"Transferases": [],\
            #"Hydrolases": [],\
            #"Lyases": [],\
            #"Isomerases": [],\
            #"Ligases": []\
            "1": [], "2": [], "3": [],\
            "4": [], "5": [], "6": []
            }
    with open(".\\RTinDB-EC.txt", "r") as f:
        while 1:
            nextline = f.readline()
            if nextline == "":
                break
            HandleRowData(nextline, spaceErrorRow, FinalRT, RTECJson)
    for i in spaceErrorRow:
        logger.error(i)
    for i in FinalRT:
        logger.info(i + str(FinalRT[i]))
    dropDB = "DROP TABLE IF EXISTS `{name}`;\n"
    createDB = "CREATE TABLE `{name}`(\n\t`ec_num` char(20) PRIMARY KEY\n);\n"
    numToRT = {"1": "Redox", "2": "Transfer", "3": "Hydrolysis",\
            "4": "Elimination", "5": "Ismerization", "6": "Ligation"}
    insertDB = "INSERT IGNORE INTO `{DB}`(ec_num) VALUES (\"{ecnum}\");\n"
    with open(".\\ErrorRows.txt", "w") as f:
        for i in spaceErrorRow:
            row = i.split(":")[0]
            row = row + "\n"
            f.write(row)
    with open(".\\RTinDB-EC_DB.sql", "w") as f:
        f.write("USE `brenda`;\n")
        for i in FinalRT:
            f.write(dropDB.format(name=numToRT[i]))
            f.write(createDB.format(name=numToRT[i]))
            for j in FinalRT[i]:
                f.write(insertDB.format(DB=numToRT[i], ecnum=j.replace("\'", "\\\"").replace("\"", "\\\"")))

@logger.catch
def handleError():
    with open(".\\RT_EC.json", "r") as f:
        RTECJson = json.load(f)
    numToRT = {"1": "Redox", "2": "Transfer", "3": "Hydrolysis",\
            "4": "Elimination", "5": "Ismerization", "6": "Ligation",\
            "7": "MustContain"}
    insertDB = "INSERT IGNORE INTO `{DB}`(ec_num) VALUES (\"{ecnum}\");\n"
    with open(".\\ErrorRowsFinal.txt", "r") as fr:
        with open(".\\RTinDB-EC_DB.sql", "a") as fw:
            while 1:
                row = fr.readline()
                if row == "":
                    break
                rowList = row.split(" ")
                for i in RTECJson[row[2:].replace("\n", "")]:
                    fw.write(insertDB.format(DB=numToRT[rowList[0]], ecnum=i.replace("\'", "\\\"").replace("\"", "\\\"")))



def HandleRowData(row: str, spaceErrorRow: list, finalRT: dict, RTECJson):
    space_list = row.split(" ")
    try:
        RTtype = int(space_list[0])
    except ValueError:
        spaceErrorRow.append(row)
        return
    colon_list = row.split(":")
    reactionName = colon_list[0][2:]
    try:
        ecList = RTECJson[reactionName]
        for i in ecList:
            if i in finalRT[str(RTtype)]:
                continue
            else:
                finalRT[str(RTtype)].append(i)
    except:
        logger.error(reactionName + ". " + row)

main()
handleError()
