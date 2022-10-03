from loguru import logger
import re

@logger.catch
def main():
    with open(".\\km_info.txt", "r") as fr:
        with open(".\\km.sql", "w") as fw:
            fw.write("USE `brenda`;\n")
            fw.write("CREATE TABLE IF NOT EXISTS `km`(id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, ec_num CHAR(20), substrate CHAR(200), speciesname CHAR(200), temp FLOAT, ph FLOAT, km FLOAT);\n")
            while 1:
                line = fr.readline()
                if line == "":
                    break
                lineList = line.split("\t")
                ec_num = lineList[0]
                speciesname = lineList[3]
                substrate = lineList[2]
                try:
                    km = float(lineList[1])
                except ValueError:
                    logger.error("[km]\t" + line)
                    continue
                temp = lineList[4].replace("\'", "\\\'")
                if "-" in temp:
                    temp = "NULL"
                else:
                    if "潞" in temp:
                        temp = re.sub("[^0-9]", "", temp)
                    try:
                        temp = float(temp)
                    except ValueError:
                        logger.error("[temp]\t" + line)
                        temp = "NULL"
                ph = lineList[5].replace("\'", "\\\'").replace("\n", "")
                if "-" in ph:
                    ph = "NULL"
                else:
                    try:
                        ph = float(ph)
                    except ValueError:
                        logger.error("[ph]\t" + line)
                        ph = "NULL"
                        continue
                fw.write(f"INSERT IGNORE INTO `km` SET ec_num=\"{ec_num}\", speciesname=\"{speciesname}\", ph={ph}, temp={temp}, substrate=\"{substrate}\", km={km};\n")

main()
