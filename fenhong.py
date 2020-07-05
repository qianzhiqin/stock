import json
import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import pyvirtualdisplay

# helper = MysqlHelper('32f64117b8.zicp.vip', 'root', 'qq84607952', 'walle')
# helper.connect()
# 请求头
url = 'http://www.iwencai.com/diag/block-detail?pid=11231&codes=000004&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%2220191231%22%2C%2220191231%22%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A7307%7D%7D%7D'

# 创建虚拟桌面
display = pyvirtualdisplay.Display(backend='xvfb', visible=False, size=(1024, 768))
display.start()
print('Initalized Display:', display.size, display.backend)

# 设置浏览器
options = webdriver.FirefoxOptions()
options.log.level = "trace" # 方便调试
options.headless = True # 无头模式

driver = webdriver.Firefox(options=options)
# driver = webdriver.Chrome()

path = os.getcwd() + '/data/list.csv'
data = pd.read_csv(path, sep=',', dtype={'symbol': str})

select_fenhong = "select * from stock where stock= %s and type= %s and user=%s and date = %s and proportion=%s "
insert_fenhong = "insert into stock (stock,type,price,source,userid,user,date,createTime,proportion) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) "

for index, row in data.iterrows():
	code = row['symbol']
	stock_name = row['name']
	try:
		url = 'http://www.iwencai.com/diag/block-detail?pid=11231&codes=' + code + '&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%2220191231%22%2C%2220191231%22%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A7307%7D%7D%7D'
		driver.get(url)
		# print(url)
		# response = requests.get(url, headers=headers).text
		response = driver.find_element_by_xpath("/html/body/pre").text
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
		res_list = stock_name + '|'
		for value in value_list:
			# print(value.text + '|', end='')
			res_list += value.text + '|'
		print(res_list)
		time.sleep(1)
	except BaseException as e:
		print(code + '|error')
driver.close()
driver.quit()
display.stop()