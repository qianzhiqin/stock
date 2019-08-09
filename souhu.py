from selenium import webdriver

import time

from selenium.common.exceptions import StaleElementReferenceException

qufu_default = '纵横双线'
browser = webdriver.Chrome()
for i in range(1, 500):
    page = 'http://tl.cyg.changyou.com/goods/selling?world_id=0&price=1-300&have_chosen=price*1-1000&page_num=' + str(
        i) + '#goodsTag'
    browser.get(page)
    server = browser.find_elements_by_class_name('server-info')
    # print('第' + str(i) + '页码')

    for i in range(0, len(server)):
        aa = server[i]
        try:
            qufu = aa.text
            title = aa.find_element_by_xpath('../../dt').text
            url = aa.find_element_by_xpath('../../dt/a').get_attribute('href')
            detail = aa.find_element_by_xpath('../../dd[1]').text
            price = aa.find_element_by_xpath('../../../div').text
            if qufu_default in qufu:
                browser.get(url)
                # row2 = browser.find_elements_by_class_name('row2')
                row2 = browser.find_element_by_xpath('//*[@id="goods-detail"]/div/div[4]/div[1]/div/div[6]/span').text
                # browser.back()
                # time.sleep(2)
                browser.get(page)
                if int(row2) >= 250:
                    print(price + '  ' + row2 + '   ' + title + '  ' + detail + '  ' + ' ' + qufu + '  ' + str(url))
        except StaleElementReferenceException as e:
            server = browser.find_elements_by_class_name('server-info')
            pass