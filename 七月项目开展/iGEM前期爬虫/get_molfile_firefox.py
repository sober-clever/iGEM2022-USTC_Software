import  selenium.webdriver as webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
import os

file = open("ec.txt")
# exc_file = open("except.txt", "w")  # 用于存无法识别的化合物
# proc_file = open("process.txt", "w")  # 用于存下载的进度


if __name__ == '__main__':
    while 1:
        ec_num = file.readline()
        if not ec_num or ec_num == "\t\n":  # 表明读到最后一行
            break
        ec_num = ec_num.replace("\n", "")  # 去掉行末的换行符
        ec_num = ec_num.replace(".", "-")  # 将 a.b.c.d 变成 a-b-c-d
        ec_num.strip()
        print(ec_num + " started")
        
        FirefoxOptions = webdriver.FirefoxOptions()

        # 不会有浏览器弹窗
        FirefoxOptions.add_argument('--headless')

        # 配置 firefox 窗口的相关选项
        fp = webdriver.FirefoxProfile()

        # 配置 firefox 下载路径
        download_path = '/home/ubuntu/mol/' + ec_num
        # 每次爬一个 EC 编码的底物 mol 文件之前新建目录
        if os.path.exists(download_path) == False:  # 如果没建这个目录则新建它
            os.makedirs(download_path)
        fp.set_preference('browser.download.dir', download_path)

        # 设置下载存储方式，2 为自定义路径
        fp.set_preference('browser.download.folderList', 2)

        # 在下载时不显示下载管理器
        fp.set_preference('browser.download.manager.showWhenStarting', False)

        #对所给出文件类型不再弹出框进行询问
        fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip,application/octet-stream')
        
        ec_file_name = r"/home/ubuntu/subpro/" + ec_num + "SubPro.txt"
        ec_file = open(ec_file_name)

        while 1:
            browser = webdriver.Firefox(options=FirefoxOptions, firefox_profile=fp)
            subpro = ec_file.readline()
            if not subpro:
                break
            subpro = subpro.replace("\n", "")
            subpro.strip()
            subpro_lis = subpro.split("\t")
            substrate = subpro_lis[0]
            substrate.strip()
            product = subpro_lis[1]
            product.strip()
            flag = 0  # 用于记录有没有超时的现象

            if substrate != "?":
                try:
                    substrate_reg = substrate.replace("(", r"%28")
                    substrate_reg = substrate_reg.replace(")", r"%29")
                    substrate_reg = substrate_reg.replace(",", r"%2C")
                    get_url = "https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=" + substrate_reg + "&T[3]=1&V[8]=1"
                    new_path = "/home/ubuntu/mol/"+ec_num+"/"+substrate+".mol"
                    if os.path.isfile(new_path) == False: # 没有这个文件，则进行下载
                        browser.get(get_url)
                        sleep(1)  # 等待网页加载完毕
                        browser.find_element(By.XPATH , "/html/body/div/div[2]/div[4]/div[2]/div[4]/a[3]").click()
                        sleep(0.5)  # 等待文件下载完毕
                        # 要确保文件下载完毕
                        t1 = time.process_time()
                        while os.path.isfile("/home/ubuntu/mol/"+ec_num+"/"+"brenda_molfile.mol") == False:
                            t2 = time.process_time()
                            if t2-t1 > 1:  # 下载超时
                                flag = 1  # 超时
                                print("TLE: " + substrate + "\n") 
                                exc_file = open("except.txt", "a")
                                exc_file.write(ec_num + " TLE: " + substrate + "\n")
                                exc_file.close()
                                raise Exception
                        os.rename("/home/ubuntu/mol/"+ec_num+"/"+"brenda_molfile.mol", new_path)
			    # 尝试下载相应的 mol 文件（注意要先判断这个 mol 文件是否存在）
                except:
                    exc_file = open("except.txt", "a")
                    exc_file.write(ec_num + " substrate: " + substrate+"\n")
                    exc_file.close()
                    # print("except: " + substrate)
                    # 表明是下载时会出现异常的化合物，要单独写到一个文件里面去
                    # 最好顺带在终端输出该化合物的名称
           
            if product != "?":
                try:
                    product_reg = product.replace("(", r"%28")
                    product_reg = product_reg.replace(")", r"%29")
                    product_reg = product_reg.replace(",", r"%2C")
                    get_url = "https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=" + product_reg + "&T[3]=1&V[8]=1"
                    new_path = "/home/ubuntu/mol/"+ec_num+"/"+product+".mol"
                    if os.path.isfile(new_path) == False: # 没有这个文件，则进行下载
                        browser.get(get_url)  # 加载网页需要时间
                        sleep(1)
                        # 如果没加载好久执行 find_element，会直接进入 except 分支
                        browser.find_element(By.XPATH , "/html/body/div/div[2]/div[4]/div[2]/div[4]/a[3]").click()
                        sleep(0.5)
                        # 如果一秒后还没下载好，就会一直等待直到下载完成
                        #（能到达这里说明是能正常下载的，只是由于网络波动，下载速度不一定稳定）
                        t1 = time.process_time()
                        while os.path.isfile("/home/ubuntu/mol/"+ec_num+"/"+"brenda_molfile.mol") == False:
                            t2 = time.process_time()
                            if t2-t1 > 1:  # 下载超时
                                flag = 1
                                print("TLE: " + product + "\n")
                                exc_file = open("except.txt", "a")
                                exc_file.write(ec_num + " TLE: " + product + "\n")
                                exc_file.close()
                                raise Exception
                        os.rename("/home/ubuntu/mol/"+ec_num+"/"+"brenda_molfile.mol", new_path)
                        # 尝试下载相应的 mol 文件（注意要先判断这个 mol 文件是否存在）
                except:
                    exc_file = open("except.txt", "a")
                    exc_file.write(ec_num + " product: " + product+"\n")
                    exc_file.close()
                    # 表明是下载时会出现异常的化合物，要单独写到一个文件里面去
                    # 最好顺带在终端输出该化合物的名称
            
            # 读完这一行后关闭浏览器
            browser.close()

                    
            if flag == 1:  # 表明有超时现象，则直接把后面的所有行都写到异常文件里面
                while 1:
                    subpro = ec_file.readline()
                    if not subpro:
                        break
                    subpro = subpro.replace("\n", "")
                    subpro.strip()
                    subpro_lis = subpro.split("\t")
                    exc_file = open("except.txt", "a")
                    exc_file.write(ec_num + "TLE: " + subpro + "\n")
                    exc_file.close()
                break

        ec_file.close()

        # 写入进度
        proc_file = open("process.txt", "a")
        proc_file.write(ec_num + " completed\n")
        proc_file.close()
       
    file.close()  # 关闭文件
