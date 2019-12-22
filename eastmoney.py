import requests
import json
import datetime

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
	
	user_list = []
	for num in range(0,8):
		params["recIdx"] = num*100
		response = requests.get(url=url, headers=headers, params=params)
		res = bytes.decode(response.content, "utf-8")
		map = json.loads(res)
		data = map["data"]
		for item in data:
			user_list.append(item)
		print(user_list.__len__())
	print(json.dumps(user_list))


def get_stock():
	today =datetime.datetime.now().strftime('%Y%m%d')
	today = "20191213"
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
	with open("./userlist", "r") as f:
		data = f.read()
		user_list = json.loads(data)
		mr_map = {}
		mc_map = {}
		mr_list = []
		mc_list = []
		for item in user_list:
			shenglv = item["rateForApp"]
			#胜率大约50才关注
			if float(shenglv) >80:
				id = item["zjzh"]
				user_name = item["zhuheName"]
				guanzhu = item["concernCnt"]
				params["zh"] = id
				response = requests.get(url=url, headers=headers, params=params)
				res = bytes.decode(response.content, "utf-8")
				map = json.loads(res)
				data = map["data"]
				for stock in data:
					name = stock["stkName"]
					date = stock["tzrq"]
					#0买，1卖
					maimai = stock["lshj_mc"]
					mc_price = stock["cjjg_mc"]
					mr_price = stock["cjjg_mr"]
					mc_bili = stock["cwhj_mc"]
					mr_bili = stock["cwhj_mr"]
					# print(stock)
					res_stock = {}
					res_stock["name"] = name
					res_stock["mr_price"] = mr_price
					res_stock["mc_price"] = mc_price
					res_stock["mr_bili"] = mr_bili
					res_stock["mc_bili"] = mc_bili
					if date == today:
						if "0" == maimai:
							if mr_map.get(name):
								mr_map[name] = mr_map[name] + 1
							else:
								mr_map[name] = 1
							# print("买 股票:" + name + "   价格:" + mr_price +" 比例: " +mr_bili)
							
							mr_list.append(res_stock)
						else:
							if mc_map.get(name):
								mc_map[name] = mc_map[name] + 1
							else:
								mc_map[name] = 1
							# print("卖 股票:" + name + "   价格:" + mc_price+" 比例: " +mc_bili)
							mc_list.append(res_stock)
		msg = "今天的日期为:" + today
		# print("====================买=======================")
		msg += "========买========" + "\n"
		for mr in mr_list:
			# print("买 股票:" + mr["name"] + "   价格:" + mr["mr_price"] + " 比例: " + mr["mr_bili"])
			msg += "买 股票:" + mr["name"] + "   价格:" + mr["mr_price"] + " 比例: " + mr["mr_bili"] + "\n"
		# print("====================卖=======================")
		msg += "=======卖========" + "\n"
		for mc in mc_list:
			# print("卖 股票:" + mc["name"] + "   价格:" + mc["mc_price"] + " 比例: " + mc["mc_bili"])
			msg += "卖 股票:" + mc["name"] + "   价格:" + mc["mc_price"] + " 比例: " + mc["mc_bili"] +"\n"
		# print("====================总=======================")
		msg += "=======总========" + "\n"
		for k,v in mr_map.items():
			if v>1:
				# print(k +"  买入出现次数 "+ str(v))
				msg += k +"  买入出现次数 "+ str(v) + "\n"
		for k,v in mc_map.items():
			if v>1:
				# print(k +"  卖出出现次数 "+ str(v))
				msg += k +"  卖出出现次数 "+ str(v) + "\n"
		# print("end")
		msg += "end"
		print(msg)
		return msg
	
if __name__ == "__main__":
    msg = get_stock()
    send_wechat(msg)