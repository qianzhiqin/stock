import requests
import json
import datetime
from MysqlHelper import *

helper = MysqlHelper('okaiok.com', 'root', 'qq84607952', 'walle')
helper.connect()

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


# 获取实盘250天总收益的用户列表
def get_user_list():
	url = "http://spzhapi.eastmoney.com/rtV1"
	params = {"type": "rt_get_rank", "rankType": "10003", "recIdx": "0", "recCnt": "100", "rankid": "0",
		"utToken": "FobyicMgeV7Y16FzbFwOUjd7IAADFJwyNdj4d9Ucxmf08vgWMsXcTWdgdSGeZAQvcL1593OBFLEj2PX5UQE2cev5oH8Q3JT0ruVIUBxZQrRJ7vJyQYJhSjQj3vgPhdIHCUb5cohXnpIKMqv5MUvXCzIXY7yvV_CoCMARORZIuD89e3iFQJhfO9qXMVbCln-YJTCmAOQvYCw2W9TWULgOpCqcbgLhUDUVy3wql-rDr-L9MSdWNcWzHA0kQPPGBtAEyPCJjeALJGgSuhM9LgpnF9JOEqi85uPKYpLnCET0n3vMgbz_hqI61g",
		"ctToken": "teGgXbepe8SCyqBjUPi5eqjsNxfaKXpbWAWUI5PoJqnqZriwTnc2uK2e8bZZ00RQAGrJ7nxJW-2SY1Jat3EpE2zcwOCb766hn2ooaw7AvgP2YkfR4OodSUBUA5MJkwC_my7yXQXQiLbmC5HHz3y9qVMinTzA6e07VE96lzkbVPM",
		"appVer": "8005001", }
	source = "eastmoney_250day"
	
	select_sql = "select id,success from user where userId = %s and user = %s "
	insert_sql = "insert into user (userId,user,source,success,createTime,updateTime) values (%s,%s,%s,%s,%s,%s)"
	update_sql = "update user set success= %s where id= %s "
	for num in range(0, 8):
		params["recIdx"] = num * 100
		response = requests.get(url=url, headers=headers, params=params)
		res = bytes.decode(response.content, "utf-8")
		map = json.loads(res)
		data = map["data"]
		for item in data:
			user_id = item["zjzh"]
			user = item["zhuheName"]
			success = item["rateForApp"]
			create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			print('start user: '+ user)
			rows = helper.fetchone(select_sql, [user_id, user])
			if not rows:
				helper.insert(insert_sql, [user_id, user, source, success, create_time, update_time])
				print("insert user " + user)
			else:
				id = rows[0]
				success_tmp = str(rows[1])
				if success != success_tmp:
					success_res = float(success)
					helper.update(update_sql, [success_res, id])
					print("update user " + user)
				else:
					print("not update user " + user)

	
if __name__ == "__main__":
	get_user_list()