import re

with open(".\\EC_Reaction_Cofactor_Database.sql", 'w') as outfile:
    outfile.write(
"""use brenda;
drop table if exists `brenda`.`reaction`;
create table `brenda`.`reaction`(
    ec_num char(20),
    reaction char(255),
    substrate char(255),
    product char(255),
    cofactor char(50),
    primary key(ec_num, reaction)
    );
""")

with open(".\\cofactor.txt", "r") as infile:
    with open(".\\EC_Reaction_Cofactor_Database.sql", 'a') as outfile:
        # ReactionList = []
        # ReactionUniqueList = []
        num = 0
        while infile:
            num = num + 1
            line = infile.readline()
            #print(line)
            lineList = line.split(",")
            for i in range(len(lineList)):
                lineList[i] = re.sub("\s+", "", lineList[i])
            if line == '':
                break
            try:
                if '?' in lineList[1] or '?' in lineList[2] or '?' in lineList[3]:
                    continue
            except:
                print(lineList)
            #ReactionList.append(lineList)
            #for i in ReactionList:
            #    if i not in ReactionUniqueList:
            #        ReactionUniqueList.append(i)
        #for lineList in ReactionUniqueList:
            try:
                if lineList[4] != '':
                    outfile.write("insert ignore into `reaction`(ec_num, reaction, substrate, product, cofactor) values (\'" + lineList[0] + "\', \'" + lineList[3] + "\', \'" + lineList[1] + "\', \'" + lineList[2] +"\', \'" + lineList[4] + "\');\n")
                else:
                    outfile.write("insert ignore into `reaction`(ec_num, reaction, substrate, product) values (\'" + lineList[0] + "\', \'" + lineList[3] + "\', \'" + lineList[1] + "\', \'" + lineList[2] + "\');\n")
            except:
                print(lineList)

            # print(num, lineList)
