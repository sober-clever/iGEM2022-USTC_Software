from time import sleep
from bs4 import BeautifulSoup
import lxml
import os
import random
import requests

file = open("ec5.txt")

header={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
"Referer": "https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=%28-%29-borneol&T[3]=1&V[8]=1",
"Upgrade-Insecure-Requests":"1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User":"?1"
}

if __name__ == "__main__":
    while 1:
        ec_num = file.readline()
        if not ec_num or ec_num == "\t\n":
            break
        ec_num = ec_num.replace("\n", "")
        ec_num = ec_num.replace(".", "-")
        ec_num.strip()
        print(ec_num + " started")
        
        # ec_file_name = ec_file_name = r"/home/ubuntu/subpro/" + ec_num + "SubPro.txt"
        ec_file_name = ".\\ec_sub_pro\\subpro\\" + ec_num + "SubPro.txt"
        ec_file = open(ec_file_name)
        
        download_path = '/home/ubuntu/mol/' + ec_num
        if os.path.exists(download_path) == False:  # 如果没建这个目录则新建它
            os.makedirs(download_path)
        
        lis = []
        
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
            if substrate != "?" and substrate not in lis:
                # print(substrate)
                substrate_reg = substrate.replace("(", r"%28")
                substrate_reg = substrate_reg.replace(")", r"%29")
                substrate_reg = substrate_reg.replace(",", r"%2C")
                get_url = "https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=" + substrate_reg + "&T[3]=1&V[8]=1"
                
                req = requests.get(url=get_url, headers=header)
                html = req.text
                bf = BeautifulSoup(html, "lxml")
                download_buttons = bf.find_all('a', class_="download")
                
                lis.append(substrate)
                
                flag = False
                
                for download_button in download_buttons:
                    link = download_button.get('href')  # 获取超链接的信息
                    if "molfile" in link:
                        LigandID = link.replace("./molfile.php?LigandID=", "")
                        # print(LigandID)
                        flag = True
                        break
                if flag: # 有 flag
                    # LigandID_file = open(download_path+"/ligand_id.txt", "a")
                    LigandID_file = open("ligand_id.txt", "a")
                    LigandID_file.write(substrate + "\t" + LigandID + "\n")
                    LigandID_file.close()
                    
                sleep(random.random())
                
            if product != "?" and product not in lis:
                # print(product)
                product_reg = product.replace("(", r"%28")
                product_reg = product_reg.replace(")", r"%29")
                product_reg = product_reg.replace(",", r"%2C")
                get_url = "https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=" + product_reg + "&T[3]=1&V[8]=1"
                
                req = requests.get(url=get_url, headers=header)
                html = req.text
                bf = BeautifulSoup(html, "lxml")
                download_buttons = bf.find_all('a', class_="download")
                
                lis.append(product)
                
                flag = False
                
                for download_button in download_buttons:
                    link = download_button.get('href')  # 获取超链接的信息
                    if "molfile" in link:
                        LigandID = link.replace("./molfile.php?LigandID=", "")
                        # print(LigandID)
                        flag = True
                        break
                if flag: # 有 flag
                    # LigandID_file = open(download_path+"/ligand_id.txt", "a")
                    LigandID_file = open("ligand_id.txt", "a")
                    LigandID_file.write(product + "\t" + LigandID + "\n")
                    LigandID_file.close()
                    
                sleep(random.random())

    # url="http://www.brenda-enzymes.org/molfile.php?LigandID=8975"


    # text=requests.get(url=url,headers=header)
    # print(text.text)
