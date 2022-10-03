from loguru import logger

@logger.catch
def main():
    with open(".\\ec_orga_info.txt", "r") as fr:
        with open(".\\ec_orga.sql", "w", encoding="utf-8") as fw:
            fw.write("USE `brenda`;\n")
            fw.write("CREATE TABLE IF NOT EXISTS `Organism`(ec_num CHAR(20), organism CHAR(200), PRIMARY KEY(ec_num, organism));\n")
            while 1:
                line = fr.readline()
                if line == "":
                    break
                lineList = line.split("\t")
                try:
                    ec_num, organism = lineList[0], lineList[1].replace("\n", "")
                except IndexError:
                    logger.error("[IndexError]\t" + line)
                fw.write(f"INSERT IGNORE INTO `organism` SET ec_num = \"{ec_num}\", organism = \"{organism}\";\n")

main()
