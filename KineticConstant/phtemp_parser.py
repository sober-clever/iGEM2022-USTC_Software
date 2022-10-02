from loguru import logger

@logger.catch
def main():
    with open(".\\ph_temp_info.txt", "r") as fr:
        with open(".\\Kinetic.sql", "w") as fw:
            fw.write("USE `brenda`;\n")
            fw.write("CREATE TABLE IF NOT EXISTS `Kinetic`(ec_num char(20), speciesname char(200), ph char(100), temp char(100), PRIMARY KEY(ec_num, speciesname));\n")
            while 1:
                line = fr.readline()
                if line == "":
                    break
                lineList = line.split("\t")
                ec_num = lineList[0]
                speciesname = lineList[1]
                temp = lineList[2].replace("\'", "\\\'")
                ph = lineList[3].replace("\'", "\\\'").replace("\n", "")
                fw.write(f"INSERT IGNORE INTO `kinetic` SET ec_num=\"{ec_num}\", speciesname=\"{speciesname}\", ph={ph}, temp={temp};\n")

main()
