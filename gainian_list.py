import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import ua_utils

ua = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: __utma=156575163.1952850795.1561647809.1561647809.1561647809.1; __utmz=156575163.1561647809.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1561647779,1561647809,1561647953; v=AjaaGTngd6AWVQPEOvIEfR_Oh2c7V3qRzJuu9aAfIpm049iRCOfKoZwr_glz
DNT: 1
Host: q.10jqka.com.cn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'''

headers = ua_utils.get_headers(ua)
path = os.getcwd() + '/data/gainian.csv'
data = pd.read_csv(path, sep=',')
url = 'http://q.10jqka.com.cn/gn/detail/field/264648/order/desc/page/1/ajax/1/code/'
# print(data)
for index, row in data.iterrows():
    code = row['code']
    neme = row['name']
    url = url + str(code)
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    list = soup.select('a[target="_blank"]')
    print(url)
    page = soup.select_one('span[class="page_info"]')
    print(page)
