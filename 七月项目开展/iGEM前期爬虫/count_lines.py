start = input()
end = input()
file = open("ec.txt")
flag = 0
cnt = 0
while 1:
    ec_num = file.readline()
    if not ec_num or ec_num == "\t\n":
        break
    ec_num = ec_num.replace("\n", "")
    if ec_num == start:
        flag = 1
    ec_num = ec_num.replace(".", "-")  # 将 a.b.c.d 变成 a-b-c-d
    ec_num.strip()
    ec_file_name = "ec_sub_pro\\subpro\\" + ec_num + "SubPro.txt" 
    ec_file = open(ec_file_name, encoding='utf-8')
    try:
        prev_cnt = cnt
        if flag == 1:
            cnt += len(ec_file.readlines())
        # for i in range(1,5):
        #     if prev_cnt < 25000*i and cnt >= 25000*i:
        #          print(ec_num + " " + str(cnt))
    except:
        print(ec_num)
    ec_file.close()
    if ec_num.replace("-", ".") == end:
        break
        
print(cnt)