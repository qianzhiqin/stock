#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

path = os.getcwd() + '/data/fund.csv'
data = pd.read_csv(path, sep=',', dtype={'symbol': str})
file_name = os.getcwd() + '/data/chicang.csv'

with open(file_name, 'w', encoding="utf-8") as file_obj:
	for index, row in data.iterrows():
		print(index)
		succ6 = row[10]
		symbol = row[0]
		name = row[1]
		if succ6 > 25:
			result = requests.get("http://fund.eastmoney.com/" + symbol + ".html", verify=False)
			result.encoding = result.apparent_encoding
			res = result.text[3:]
			soup = BeautifulSoup(res, 'lxml')
			stock_zhai = soup.select('div[class="poptableWrap"] table[class="ui-table-hover"]')
			for item in stock_zhai:
				for tr in item:
					# 判断只有不为NavigableString类型才可以继续
					if str(type(tr)) != "<class 'bs4.element.NavigableString'>":
						tmp = tr.text.strip()
						if "股票名称" not in tmp and "债券名称" not in tmp:
							val = tmp.split(' ')
							if len(val) == 6:
								stock = symbol + '\t' + name + '\t' + str(succ6) + '\t' + val[0] + '\t' + val[2].replace('%', '')
								file_obj.write(stock + "\n")
								print(stock)
							elif len(val) == 5:
								stock = symbol + '\t' + name + '\t' + str(succ6) + '\t' + val[0] + '\t' + val[3].replace('%', '')
								file_obj.write(stock + "\n")
								print(stock)
		file_obj.flush()
