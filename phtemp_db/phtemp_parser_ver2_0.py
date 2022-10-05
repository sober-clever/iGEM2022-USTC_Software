from loguru import logger

@logger.catch
def main():
    with open(".\\ph_temp_info.txt", "r") as fr:
        with open(".\\phtemp.sql", "w") as fw:
            fw.write("USE `brenda`;\n")
            fw.write("CREATE TABLE IF NOT EXISTS `Phtemp`(id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, ec_num CHAR(20), speciesname CHAR(200), ph CHAR(100), temp CHAR(100), literture CHAR(20));\n")
            while 1:
                line = fr.readline()
                if line == "":
                    break
                lineList = line.split("\t")
                ec_num = lineList[0]
                speciesname = lineList[1]
                #ph = lineList[2].replace("\'", "\\\'")
                #temp = lineList[3].replace("\'", "\\\'")
                ph = lineList[2].replace("\'", "")
                temp = lineList[3].replace("\'", "")
                literture = lineList[4].replace("\n", "")
                fw.write(f"INSERT IGNORE INTO `Phtemp` SET ec_num=\"{ec_num}\", speciesname=\"{speciesname}\", ph={ph}, temp={temp}, literture=\"{literture}\";\n")

main()
