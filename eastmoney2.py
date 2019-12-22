import requests
import json
import datetime
import sqlite3

def get_connect():
	return  sqlite3.connect('stock.db')

def send_wechat(content):
	requests.packages.urllib3.disable_warnings()
	params = {'corpid': 'wx48550600b1a01730',
	          'corpsecret': 'sYreGwLC6f4wZusDqynBPMpHYyg8s_-bJUQLdHGeOxUbHhvcMvBbOyZQZMZDwsrD'}
	result = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params ,verify=False)
	access_token = None
	if result.status_code != 200:
		print('连接到服务器失败')
	else:
		result_json = json.loads(result.text)
		if result_json['errcode'] != 0:
			print('响应结果不正确')
		else:
			access_token = result_json['access_token']
			print("获取token成功： "+ access_token)
	data_params = {
		"touser": "@all",
		"msgtype": "text",
		"agentid": 2,
		"text": {
            "content": content
         },
	    "safe": 0}
	result = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(access_token),
	                       data=json.dumps(data_params),verify=False)
	print("发送微信状态: " + str(result.status_code))

# 请求头
headers = {
	"Host":"spzhapi.eastmoney.com",
	"Connection":"keep-alive",
	"Accept":"*/*",
	"User-Agent":"app-iphone-client-iPhone10,3-10F1F08F-CE14-4158-9B7B-1D14C9A1166C",
	"Accept-Language":"zh-cn",
	"Accept-Encoding":"gzip",
	"Connection":"keep-alive"
}

#获取实盘250天总收益的用户列表
def get_user_list():
	url = "http://spzhapi.eastmoney.com/rtV1"
	params = {
		"type":"rt_get_rank",
		"rankType":"10003",
		"recIdx":"0",
		"recCnt":"100",
		"rankid":"0",
		"utToken":"FobyicMgeV7Y16FzbFwOUjd7IAADFJwyNdj4d9Ucxmf08vgWMsXcTWdgdSGeZAQvcL1593OBFLEj2PX5UQE2cev5oH8Q3JT0ruVIUBxZQrRJ7vJyQYJhSjQj3vgPhdIHCUb5cohXnpIKMqv5MUvXCzIXY7yvV_CoCMARORZIuD89e3iFQJhfO9qXMVbCln-YJTCmAOQvYCw2W9TWULgOpCqcbgLhUDUVy3wql-rDr-L9MSdWNcWzHA0kQPPGBtAEyPCJjeALJGgSuhM9LgpnF9JOEqi85uPKYpLnCET0n3vMgbz_hqI61g",
		"ctToken":"teGgXbepe8SCyqBjUPi5eqjsNxfaKXpbWAWUI5PoJqnqZriwTnc2uK2e8bZZ00RQAGrJ7nxJW-2SY1Jat3EpE2zcwOCb766hn2ooaw7AvgP2YkfR4OodSUBUA5MJkwC_my7yXQXQiLbmC5HHz3y9qVMinTzA6e07VE96lzkbVPM",
		"appVer":"8005001",
	}
	source = "eastmoney"


	select_sql = "select userId,success from user where userId = ? and user = ? ;"
	insert_sql = "insert into user (userId,user,source,success,createTime,updateTime) values (?,?,?,?,?,?);"
	update_sql = "update  user set  success= ? where id= ? ;"
	for num in range(0,8):
		params["recIdx"] = num*100
		response = requests.get(url=url, headers=headers, params=params)
		res = bytes.decode(response.content, "utf-8")
		map = json.loads(res)
		data = map["data"]
		for item in data:
			conn = get_connect()
			cursor = conn.cursor()
			user_id = item["zjzh"]
			user = item["zhuheName"]
			success = item["rateForApp"]
			create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		
			rows = cursor.execute(select_sql,(user_id,user))
			# print(len(list(rows)))
			length = len(list(rows))
			if length <= 0 :
				cursor.execute(insert_sql, (user_id, user, source, success, create_time, update_time))
				conn.commit()
				print("insert user " +user)
			else:
				for row in rows:
					id = row[0]
					success_tmp = row[1]
					if success != success_tmp:
						cursor.execute(update_sql, (success_tmp, id))
						conn.commit()
						print("update user " + user)
			conn.close()
def get_stock():
	today =datetime.datetime.now().strftime('%Y%m%d')
	today = "20191220"
	print("今天的日期为:" + today)
	url = "http://spzhapi.eastmoney.com/rtV1"
	params = {
		"type": "rt_hold_change72",
		"zh": "900004656",
		"recIdx": "1",
		"recCnt": "10",
		"reqUserid": "1110114787578370",
		"utToken": "FobyicMgeV7Y16FzbFwOUjd7IAADFJwyNdj4d9Ucxmf08vgWMsXcTWdgdSGeZAQvcL1593OBFLEj2PX5UQE2cev5oH8Q3JT0ruVIUBxZQrRJ7vJyQYJhSjQj3vgPhdIHCUb5cohXnpIKMqv5MUvXCzIXY7yvV_CoCMARORZIuD89e3iFQJhfO9qXMVbCln-YJTCmAOQvYCw2W9TWULgOpCqcbgLhUDUVy3wql-rDr-L9MSdWNcWzHA0kQPPGBtAEyPCJjeALJGgSuhM9LgpnF9JOEqi85uPKYpLnCET0n3vMgbz_hqI61g",
		"ctToken": "teGgXbepe8SCyqBjUPi5eqjsNxfaKXpbWAWUI5PoJqnqZriwTnc2uK2e8bZZ00RQAGrJ7nxJW-2SY1Jat3EpE2zcwOCb766hn2ooaw7AvgP2YkfR4OodSUBUA5MJkwC_my7yXQXQiLbmC5HHz3y9qVMinTzA6e07VE96lzkbVPM",
		"appVer": "8005001",
	}
	select_user=  "select userId,user,success from user where  cast(success as DOUBLE) > 100;"
	conn = get_connect()
	cursor = conn.cursor()
	rows = cursor.execute(select_user)
	select_stock = "select * from stock where stock=? and type=? and user=? and date = ?  and proportion=?"
	insert_stock = "insert into stock (stock,type,price,source,userid,user,date,createTime,proportion) values (?,?,?,?,?,?,?,?,?)"
	count = 0
	for row in rows:
		user_id= row[0]
		user= row[1]
		success= row[2]
		params["zh"] = user_id
		response = requests.get(url=url, headers=headers, params=params)
		res = bytes.decode(response.content, "utf-8")
		map = json.loads(res)
		data = map["data"]
	
		for stock_info in data:
			stock = stock_info["stkName"]
			date = stock_info["tzrq"]
			#0买，1卖
			maimai = stock_info["lshj_mc"]
			mc_price = stock_info["cjjg_mc"]
			mr_price = stock_info["cjjg_mr"]
			mc_bili = stock_info["cwhj_mc"]
			mr_bili = stock_info["cwhj_mr"]
		 
			if date == today:
				source = "eastmoney"
				create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				# 0为买
				if "0" == maimai:
					type = "买"
					price = mr_price
					proportion = mr_bili
				else:
					type = "卖"
					price = mc_price
					proportion = mc_bili
				cursor2 = conn.cursor()
				rows2 = cursor2.execute(select_stock,(stock, type, user, date, proportion))
				if len(list(rows2)) <= 0:
					cursor2.execute(insert_stock,(stock,type,price,source,user_id,user,date,create_time,proportion) )
					conn.commit()
					count +=1
	print("插入了 " +str(count))
	conn.close()
	
		
	
if __name__ == "__main__":
    # msg = get_stock()
    # send_wechat(msg)
	get_stock()