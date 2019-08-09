from selenium import webdriver

qufu_default = '纵横双线'
browser = webdriver.Chrome()
for i in range(1, 500):
	browser.get(
		'http://tl.cyg.changyou.com/goods/selling?world_id=0&price=1-1000&have_chosen=price*1-1000&page_num=' + str(
			i) + '#goodsTag')
	server = browser.find_elements_by_class_name('server-info')
	# print('第' + str(i) + '页码')
	for aa in server:
		qufu = aa.text
		title = aa.find_element_by_xpath('../../dt').text
		detail = aa.find_element_by_xpath('../../dd[1]').text
		price = aa.find_element_by_xpath('../../../div').text
		if qufu_default in qufu:
			print(price + '   ' + title + '  ' + detail + '  ' + aa.text)
