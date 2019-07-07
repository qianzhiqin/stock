import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

path = os.getcwd() + '/data/gainian.csv'
data = pd.read_csv(path, sep=',')
url = 'http://q.10jqka.com.cn/gn/detail/field/264648/order/desc/page/1/ajax/1/code/'
# print(data)
for index, row in data.iterrows():
	code = row['code']
	neme = row['name']
	url = url + str(code)
	response = requests.get(url)
	print(response)
