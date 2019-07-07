import requests
from bs4 import BeautifulSoup
from lxml import html
import os

from html.parser import HTMLParser

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#     ,
#     'Cookie': '__utma=156575163.1952850795.1561647809.1561647809.1561647809.1; __utmz=156575163.1561647809.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1561647779,1561647809,1561647953; v=AgunGrT30snkwQ6dHWCBjmpRmqT2oB8DmbTj1n0I58qhnCUSBXCvcqmEcy-O'
# }
# response = requests.get("http://q.10jqka.com.cn/gn/", headers=headers)
# data = response.text
# print(response.status_code)
file_name = r'C:\\Users\\qianzhiqin\\Desktop\\abc.txt'
f = open(file_name, 'r')
data = f.read()
# print(data)
soup = BeautifulSoup(data, "lxml")
aaa = soup.find_all('div', class_ ="cate_items")
# content = soup.find_all('div', class_="cate_items")
bbb = BeautifulSoup(str(aaa), "lxml").find_all('a', target='_blank')
for i in bbb:
    # print(i)
    soup_i = BeautifulSoup(str(i), "lxml").find_all('a')[0]
    href = soup_i['href']
    value = soup_i.text
    if href.startswith('http://q.10jqka.com.cn/gn/detail/code'):
        code = href.split('/')[6]
        # print(i)
        print(code + ',' + value)
