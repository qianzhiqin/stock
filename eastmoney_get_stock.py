import requests
import json
import datetime
from MysqlHelper import *

helper = MysqlHelper('okaiok.com', 'root', 'qq84607952', 'walle')
helper.connect()

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

def get_stock():
	today =datetime.datetime.now().strftime('%Y%m%d')
	# today = "20191101"
	print("今天的日期为:" + today)
	url = "http://spzhapi.eastmoney.com/rtV1"
	params = {
		"type": "rt_hold_change72",
		"zh": "900004656",
		"recIdx": "1",
		"recCnt": "100",
		"reqUserid": "1110114787578370",
		"utToken": "FobyicMgeV7Y16FzbFwOUjd7IAADFJwyNdj4d9Ucxmf08vgWMsXcTWdgdSGeZAQvcL1593OBFLEj2PX5UQE2cev5oH8Q3JT0ruVIUBxZQrRJ7vJyQYJhSjQj3vgPhdIHCUb5cohXnpIKMqv5MUvXCzIXY7yvV_CoCMARORZIuD89e3iFQJhfO9qXMVbCln-YJTCmAOQvYCw2W9TWULgOpCqcbgLhUDUVy3wql-rDr-L9MSdWNcWzHA0kQPPGBtAEyPCJjeALJGgSuhM9LgpnF9JOEqi85uPKYpLnCET0n3vMgbz_hqI61g",
		"ctToken": "teGgXbepe8SCyqBjUPi5eqjsNxfaKXpbWAWUI5PoJqnqZriwTnc2uK2e8bZZ00RQAGrJ7nxJW-2SY1Jat3EpE2zcwOCb766hn2ooaw7AvgP2YkfR4OodSUBUA5MJkwC_my7yXQXQiLbmC5HHz3y9qVMinTzA6e07VE96lzkbVPM",
		"appVer": "8005001",
	}
	select_user=  "select userId,user,success from user where success > 100 "
	select_stock = "select * from stock where stock= %s and type= %s and user=%s and date = %s and proportion=%s "
	insert_stock = "insert into stock (stock,type,price,source,userid,user,date,createTime,proportion) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
	rows = helper.fetchall(select_user)
	source = "eastmoney_250day"

	for row in rows:
		user_id= row[0]
		user= row[1]
		success= row[2]
		params["zh"] = user_id
		response = requests.get(url=url, headers=headers, params=params)
		res = bytes.decode(response.content, "utf-8")
		map = json.loads(res)
		data = map["data"]
		
		print("start user: " + user)
		count = 0
		for stock_info in data:
			stock = stock_info["stkName"]
			date = stock_info["tzrq"]
			#0买，1卖
			mc_bishu = stock_info["lshj_mc"]
			mr_bishu = stock_info["lshj_mr"]
			mc_price = stock_info["cjjg_mc"]
			mr_price = stock_info["cjjg_mr"]
			mc_bili = stock_info["cwhj_mc"]
			mr_bili = stock_info["cwhj_mr"]
		
			if date == today:
				create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				# 买
				if "0" == mc_bishu:
					type = "买"
					price = mr_price
					proportion = mr_bili
				else:
					type = "卖"
					price = mc_price
					proportion = mc_bili
				 
				rows2 = helper.fetchone(select_stock,[stock, type, user, date, proportion])
				if not rows2:
					helper.insert(insert_stock,[stock,type,price,source,user_id,user,date,create_time,proportion] )
					count +=1
		print("end user count： " +str(count))
	
		
	
if __name__ == "__main__":
	get_stock()