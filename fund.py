#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import datetime
from MysqlHelper import *

ua = """"Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: searchbar_code=100032; qgqp_b_id=56877fffcad6f4090071620a9edaf83b; xsb_history=835727%7C%u4E92%u8054%u5728%u7EBF; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; st_si=42402717726643; st_asi=delete; ASP.NET_SessionId=2vu31m2bksibg0shjotqgmw3; EMFUND0=null; EMFUND5=09-29%2020%3A08%3A42@%23%24%u534E%u5B9D%u6807%u666E%u7F8E%u56FD%u6D88%u8D39%u4EBA%u6C11%u5E01A@%23%24162415; EMFUND6=09-29%2020%3A10%3A25@%23%24%u535A%u65F6%u519B%u5DE5%u4E3B%u9898%u80A1%u7968@%23%24004698; EMFUND7=10-24%2018%3A09%3A21@%23%24%u957F%u76DB%u521B%u65B0%u9A71%u52A8%u7075%u6D3B%u914D%u7F6E%u6DF7%u5408@%23%24004745; EMFUND8=10-24%2018%3A16%3A29@%23%24%u4E2D%u6D77%u73AF%u4FDD%u65B0%u80FD%u6E90%u6DF7%u5408@%23%24398051; EMFUND9=11-03 20:13:06@#$%u7EA2%u571F%u521B%u65B0%u65B0%u5174%u4EA7%u4E1A%u6DF7%u5408@%23%24001753; _adsame_fullscreen_14694=1; st_pvi=46401995016240; st_sp=2020-08-05%2019%3A46%3A36; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=17; st_psi=20201107164029333-0-7877612722
DNT: 1
Host: fund.eastmoney.com
Referer: http://fund.eastmoney.com/data/fundranking.html
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"""


def get_ua():
	headers = {}
	lines = ua.split('\n')
	for line in lines:
		kv = line.split(": ")
		headers[kv[0]] = kv[1]
	return headers


helper = MysqlHelper('okaiok.com', 'root', 'qq84607952', 'walle')
# helper = MysqlHelper('localhost', 'root', 'qq84607952', 'walle')
helper.connect()

select_sql = "SELECT id,code FROM fund WHERE code = %s "
insert_sql = "INSERT INTO  fund (code,name,alias,date,dwjz,ljjz,day1,week1,month1,month3,month6,year1,year2,year3,thisyear,chenglilai,chengliday,shouxufei) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
update_sql = "UPDATE fund SET  name = %s, alias = %s, date = %s, dwjz = %s, ljjz= %s, day1 = %s, week1 = %s, month1 = %s, month3 = %s, month6 = %s, year1 = %s, year2 = %s, year3 = %s, thisyear = %s, chenglilai = %s, chengliday = %s, shouxufei = %s WHERE code = %s "

headers = get_ua()
today = datetime.datetime.now().strftime('%Y-%m-%d')
yearago = (datetime.datetime.now() + datetime.timedelta(days=-366)).strftime('%Y-%m-%d')
print(today +' 开始更新.')
result = requests.get(
	"http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=" + yearago + "&ed=" + today + "&qdii=&tabSubtype=,,,,,&pi=1&pn=10000&dx=1&v=0.9102788336446412",
	headers=headers, verify=False)

res = result.text.replace("var rankData = {datas:", "").split(',allRecords:')[0]
# print(res)
data = json.loads(res)
print("列表长度为: " + str(len(data)))
for item in data:
	split = str(item).split(',')
	code = split[0]
	selectArr = []
	insertArr = []
	updateArr = []
	selectArr.append(code)
	rows = helper.fetchone(select_sql, selectArr)
	for i in range(len(split)):
		if i < 17 or i == 20:
			# print(split[i], end=',')
			if split[i] == '':
				insertArr.append(0)
				updateArr.append(0)
			else:
				insertArr.append(split[i])
				updateArr.append(split[i])
	# print()
	updateArr.remove(code)
	updateArr.append(code)
	if not rows:
		a = helper.insert(insert_sql, insertArr)
		print("insert  " + code)
	else:
		b = helper.update(update_sql, updateArr)
		print("update " + code )
print(today +' 更新完成.')