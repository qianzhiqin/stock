import requests
from ua_utils import *
import json


def longtou(url):
	headers = get_ua()
	# url = 'http://www.iwencai.com/stockpick/cache?token=ed3c66a57283e2166345c5a26b766608&p=1&perpage=200&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]'
	response = requests.get(url, headers=headers)
	res = response.text
	content = json.loads(res)
	result = content['result']
	for line in result:
		code = line[0]
		name = line[1]
		hangye1 = line[4]
		hangye3 = line[5]
		print("%s,%s,%s,%s" % (code, name, hangye1, hangye3))


url1 = 'http://www.iwencai.com/stockpick/cache?token=ed3c66a57283e2166345c5a26b766608&p=1&perpage=200&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]'
url2 = 'http://www.iwencai.com/stockpick/cache?token=6ee73e3c5c559ca1e8fea40e61585606&p=1&perpage=500&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]'
url3 = 'http://www.iwencai.com/stockpick/cache?token=16b02a459afa6218212d13cd6945eadb&p=1&perpage=700&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]'
longtou(url3)
