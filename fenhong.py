import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import ua_utils
import json
import time

ua = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Cookie: PHPSESSID=1efd6514f9e7446ed6ef1613491bdf95; cid=1efd6514f9e7446ed6ef1613491bdf951592364712; ComputerID=1efd6514f9e7446ed6ef1613491bdf951592364712; WafStatus=1; guideState=1; v=Ao_rgMHlDW_wQgmTDlRfgt-QHiiatOPQfQjnyqGcK_4FcKGeqYRzJo3YdxOy
DNT: 1
Host: www.iwencai.com
Proxy-Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'''

url = 'http://www.iwencai.com/diag/block-detail?pid=11231&codes=000004&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%2220191231%22%2C%2220191231%22%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A7307%7D%7D%7D'

headers = ua_utils.get_ua(ua)
path = os.getcwd() + '/data/list.csv'
data = pd.read_csv(path, sep=',', dtype={'symbol': str})

select_fenhong = "select * from stock where stock= %s and type= %s and user=%s and date = %s and proportion=%s "
insert_fenhong = "insert into stock (stock,type,price,source,userid,user,date,createTime,proportion) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) "

for index, row in data.iterrows():
	code = row['symbol']
	stock_name = row['name']
	try:
		url = 'http://www.iwencai.com/diag/block-detail?pid=11231&codes=' + code + '&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%2220191231%22%2C%2220191231%22%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A7307%7D%7D%7D'
		
		# print(url)
		response = requests.get(url, headers=headers).text
		# print(response)
		res = json.loads(response)
		html = res['data']['data']['result'][0]['item']['tableTempl']
		
		soup = BeautifulSoup(html, 'lxml')
		# print(soup)
		if index == 0:
			name_list = soup.select('span[class="th_words"]')
			name_tmp = '股票名字|'
			for name in name_list:
				# print(name.text +'|',end='')
				name_tmp += name.text + '|'
			print(name_tmp)
		# value_list = soup.select('div[class="em"]')
		value_list = soup.find_all(name="div", attrs={"class": "em"})
		res_list = stock_name+'|'
		for value in value_list:
			# print(value.text + '|', end='')
			res_list += value.text + '|'
		print(res_list)
		time.sleep(0.3)
	except BaseException:
		print(code + '|error')