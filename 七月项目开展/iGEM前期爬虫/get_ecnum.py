import requests
import lxml
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

if __name__ == '__main__':
    target = 'https://www.brenda-enzymes.org/all_enzymes.php'
    req = requests.get(url=target, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, "lxml")
    
    cells = bf.find_all('div', class_ = 'cell')   # 找出所有 class 为 row ，rows 为一个列表
    
    file = "ec.txt"
    for cell in cells:
        s = cell.text
        if s[0] in "0123456789" and s[1]=='.': # 第一个字符是数字
            with open(file, mode="a", encoding="utf-8") as f:
                f.write(s)
                f.write("\n")
    
    # print(req.text)