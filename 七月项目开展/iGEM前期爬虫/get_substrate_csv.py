#从inchi转为分子图

import urllib
from urllib.request import urlretrieve
from time import sleep
import random

file = open("ec.txt")

if __name__ == '__main__':
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    while 1:
        line = file.readline()
        if not line:
            break
        line = line.replace("\n", "")
        csv_url = "https://www.brenda-enzymes.org/result_download.php?a=37&W[1]=" + line
        csv_url = csv_url + "&T[1]=1&os=1&nolimit=1&V[6]=1"
        # mol_url = r"https://www.brenda-enzymes.org/search_result.php?quicksearch=1&noOfResults=10&a=13&W[3]=%281S%2C3S*%29-3-methylcyclohexanol&T[3]=2&V[8]=1"
        filename = line.replace(".","-")
        path = "./csv/" + filename + ".csv";
        urlretrieve(csv_url, path) #将什么文件存放到什么位置
        sleep(random.randint(15,30))