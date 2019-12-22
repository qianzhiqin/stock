import json
import requests

def send_wechat(content, user):
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
	print(result.status_code)

if __name__ == "__main__":
	send_wechat("do test.", None)
