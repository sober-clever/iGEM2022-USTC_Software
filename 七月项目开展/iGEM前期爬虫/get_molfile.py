# from operator import sub
# from numpy import product
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.select import Select


chromeOptions = webdriver.ChromeOptions()

# 配置 下载的弹窗设置 和 下载路径
prefs = {   "profile.default_content_settings.popups":0,
            "download.default_directory":r"C:\Users\Tanjf\Desktop\iGEM\mol"}

chromeOptions.add_experimental_option("prefs", prefs)

# 自动运行时不显示 chrome 浏览器窗口
chromeOptions.add_argument('headless')
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging']) 

# 配置 chrome 窗口的相关选项
browser = webdriver.Chrome(options=chromeOptions)

file = open("ec.txt")

proc_file = open("process.txt", "w")  # 用于存下载的进度


if __name__ == '__main__':
    while 1:
        ec_num = file.readline()
        if not ec_num or ec_num=="\t\n":  # 表明读到最后一行
            break
        ec_num = ec_num.replace("\n", "")  # 去掉行末的换行符
        ec_num = ec_num.replace(".", "-")  # 将 a.b.c.d 变成 a-b-c-d
        ec_num.strip()
        print(ec_num + " started")
        ec_file_name = "ec_sub_pro\\subpro\\" + ec_num + "SubPro.txt" 
        ec_file = open(ec_file_name)

        while 1:
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
            # print(substrate + " " + product)
            if substrate != "?":
                try:
                    substrate_reg = substrate.replace("(", r"%28")
                    substrate_reg = substrate_reg.replace(")", r"%29")
                    substrate_reg = substrate_reg.replace(",", r"%2C")
                    get_url = "https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=" + substrate_reg + "&T[3]=1&V[8]=1"
                    new_path = "C:\\Users\\Tanjf\\Desktop\\iGEM\mol\\"+substrate+".mol"
                    if os.path.isfile(new_path) == False: # 没有这个文件，则进行下载
                        browser.get(get_url)
                        sleep(0.5)
                        browser.find_element(By.XPATH , "/html/body/div/div[2]/div[4]/div[2]/div[4]/a[3]").click()
                        sleep(0.5)
                        os.rename(r"C:\Users\Tanjf\Desktop\iGEM\mol\brenda_molfile.mol", new_path)
                        # 尝试下载相应的 mol 文件（注意要先判断这个 mol 文件是否存在）
                except:
                    exc_file = open("except.txt", "a")  # 用于存无法识别的化合物
                    exc_file.write(substrate+"\n")
                    exc_file.close()
                    print("except: " + substrate)
                    # 表明是下载时会出现异常的化合物，要单独写到一个文件里面去
                    # 最好顺带在终端输出该化合物的名称
            
            if product != "?":
                try:
                    product_reg = product.replace("(", r"%28")
                    product_reg = product_reg.replace(")", r"%29")
                    product_reg = product_reg.replace(",", r"%2C")
                    get_url = "https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=" + product_reg + "&T[3]=1&V[8]=1"
                    new_path = "C:\\Users\\Tanjf\\Desktop\\iGEM\mol\\"+product+".mol"
                    if os.path.isfile(new_path) == False: # 没有这个文件，则进行下载
                        browser.get(get_url)  # 加载网页需要时间
                        sleep(0.5)
                        browser.find_element(By.XPATH , "/html/body/div/div[2]/div[4]/div[2]/div[4]/a[3]").click()
                        sleep(0.5)
                        os.rename(r"C:\Users\Tanjf\Desktop\iGEM\mol\brenda_molfile.mol", new_path)
                        # 尝试下载相应的 mol 文件（注意要先判断这个 mol 文件是否存在）
                except:
                    exc_file = open("except.txt", "a")  # 用于存无法识别的化合物
                    exc_file.write(product+"\n")
                    exc_file.close()
                    print("except: " + product)
                    # 表明是下载时会出现异常的化合物，要单独写到一个文件里面去
                    # 最好顺带在终端输出该化合物的名称
        
        ec_file.close()
        proc_file.write(ec_num + " completed\n")
        
        # browser.get("https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=hydroxypyruvate&T[3]=1&V[8]=1")

        # sleep(3)
        # browser.find_element(By.XPATH , "/html/body/div/div[2]/div[4]/div[2]/div[4]/a[3]").click()

        # sleep(2)
        # os.rename(r"C:\Users\Tanjf\Desktop\mol\brenda_molfile.mol", r"C:\Users\Tanjf\Desktop\iGEM\mol\hydroxypyruvate.mol")
    proc_file.close()
    exc_file.close()
    file.close()  # 关闭文件