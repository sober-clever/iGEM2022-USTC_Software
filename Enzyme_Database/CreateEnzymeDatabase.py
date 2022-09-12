with open(".\\CreateEnzymeDatabase.sql", "w") as outfile:
    text = "use brenda;\n"\
            + "create table `enzyme`(\n"\
            + "\tec_num char(20) primary key,\n"\
            + "\tec_name char(100)\n"\
            + ");\n"
    outfile.write(text)

with open(".\\ec_name.txt", "r") as infile:
    with open(".\\CreateEnzymeDatabase.sql", "a") as outfile:
        while infile:
            try:
                line = infile.readline()
            except:
                print("[Not read]" + line)
            lineList = line.split("\t")
            if line == '':
                break
            try:
                outfile.write("insert ignore into `brenda`.`enzyme`(ec_num, ec_name) values(\'{ec_num}\', \'{ec_name}\');\n".format(ec_num = lineList[0], ec_name = lineList[1].replace("\n", "").replace("\'", "\'\'")))
            except:
                print("[Not written]" + line)

# Error handling
with open(".\\CreateEnzymeDatabase.sql", "a") as outfile:
    text = "insert ignore into `brenda`.`enzyme`(ec_num, ec_name) values(\'{ec_num}\', \'{ec_name}\');\n".format(ec_num = "1.14.19.16", ec_name = "linoleoyl-lipid DELTA12 conjugase (11e,13Z-forming)")
    outfile.write(text)
