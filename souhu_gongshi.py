from selenium import webdriver
# from cookie_utils import set_cookies
import time

from selenium.common.exceptions import StaleElementReferenceException

qufu_default = '纵横双线'
browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.set_script_timeout(30)
browser.get('http://tl.cyg.changyou.com/goods/public')
cookie_list =[{"domain":".changyou.com","expirationDate":1627687974,"hostOnly":False,"httpOnly":False,"name":"_ga","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"GA1.2.332667585.1562338662","id":1},{"domain":".changyou.com","expirationDate":1595432217,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_1c6f42e977ee44f0c20dc8082d990ae3","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1563286295,1563896217","id":2},{"domain":".changyou.com","hostOnly":False,"httpOnly":False,"name":"IMGCODE","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"ImageCode-87708-83f1c12d-8e54-447c-9d8b-4113d22b1c69-NxTuD9","id":3},{"domain":".changyou.com","expirationDate":87962252258,"hostOnly":False,"httpOnly":False,"name":"macid","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"C882B56E9A300001921325E413001E72","id":4},{"domain":".changyou.com","expirationDate":2147385600,"hostOnly":False,"httpOnly":False,"name":"pgv_pvi","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"7326088116","id":5},{"domain":".changyou.com","hostOnly":False,"httpOnly":False,"name":"qrcodeid","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"2f583b720a56470baaad9424adcedb89610ae48b833a500ffe8bd3f5ee49b6c0e591985aa9d023989e38fa5262535a67","id":6},{"domain":".changyou.com","expirationDate":1567696915.724857,"hostOnly":False,"httpOnly":False,"name":"Ta3u_7428_lastvisit","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1565101316","id":7},{"domain":".changyou.com","expirationDate":1567696915.724806,"hostOnly":False,"httpOnly":True,"name":"Ta3u_7428_saltkey","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"uy25X788","id":8},{"domain":".changyou.com","expirationDate":1567696915.72503,"hostOnly":False,"httpOnly":False,"name":"Ta3u_7428_visitedfid","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"510D1590","id":9},{"domain":".changyou.com","expirationDate":1582597765,"hostOnly":False,"httpOnly":False,"name":"UM_distinctid","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"16cd0e81291248-0541e56e998da2-e343166-144000-16cd0e812924c6","id":10},{"domain":".cyg.changyou.com","expirationDate":1598576215,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_416c770ac83a9d996d7b3793f8c4994d","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1567005927,1567040216","id":11},{"domain":".cyg.changyou.com","expirationDate":1598408964,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1566872964","id":12},{"domain":".tl.cyg.changyou.com","expirationDate":1598577113,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_416c770ac83a9d996d7b3793f8c4994d","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1567005927,1567040216","id":13},{"domain":".tl.cyg.changyou.com","expirationDate":1598409644,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1566872964","id":14},{"domain":"tl.cyg.changyou.com","expirationDate":1657033486,"hostOnly":True,"httpOnly":False,"name":"bdshare_firstime","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1562339086226","id":15},{"domain":"tl.cyg.changyou.com","expirationDate":1583417617,"hostOnly":True,"httpOnly":False,"name":"CNZZDATA5373220","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"cnzz_eid%3D259278903-1567690571-http%253A%252F%252Ftl.cyg.changyou.com%252F%26ntime%3D1567690571","id":16},{"domain":"tl.cyg.changyou.com","expirationDate":1583419363,"hostOnly":True,"httpOnly":False,"name":"CNZZDATA5453193","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"cnzz_eid%3D402477452-1566871454-http%253A%252F%252Fcyg.changyou.com%252F%26ntime%3D1567692478","id":17},{"domain":"tl.cyg.changyou.com","expirationDate":1599230525.180892,"hostOnly":True,"httpOnly":False,"name":"COOKIE_GOODS_SCANED","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"%25E5%25AE%2589%25E7%25AC%2591%25E8%25A8%2580%25E3%2581%25A4%253D20190829846286107%253D150.0%253D12%2527%25C2%25B7%25E8%25A7%2589%25E6%2582%259F%25C2%25B7%253D201909022040525670%253D261.0%253D8%2527%25E6%259F%2594%25E6%2583%2585%25E7%259A%2584%25E7%2596%25AF%25E5%25AD%2590%253D201909021801563245%253D251.0%253D2%2527%25E4%25B9%2584%25E7%2581%25ACDear%25E7%2581%25AC%25E5%25AF%25B6%253D201908221400532393%253D200.0%253D8%2527%25E6%259F%25B3%25E6%259C%25A8%253D201908251307557738%253D200.0%253D8","id":18},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":True,"name":"JSESSIONID","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"E91B696A11F36FD2ED58DBBFC35ADF6D","id":19},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":False,"name":"NOTE_CACHE","path":"/goods","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"%5B%7B%22id%22%3A200%2C%22title%22%3A%22%E6%B5%8B%E6%9C%8D%E9%BE%99%E9%97%A8NPC%E7%BB%B4%E6%8A%A4%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1432711191000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A198%2C%22title%22%3A%22%E5%AE%A0%E7%88%B1%E4%B8%80%E7%94%9F%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BB%B4%E6%8A%A4%E5%AE%8C%E6%88%90%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1431314942000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A197%2C%22title%22%3A%22%E5%AE%A0%E7%88%B1%E4%B8%80%E7%94%9F%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BB%B4%E6%8A%A4%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1431312451000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A196%2C%22title%22%3A%22%E3%80%904%E6%9C%8817%E6%97%A5%E7%BB%B4%E6%8A%A4%E3%80%91%E7%95%85%E6%98%93%E9%98%81.%E9%81%93%E5%85%B7%E5%9D%8A%E7%BB%B4%E6%8A%A4%E5%85%AC%E5%91%8A%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1429156000000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A192%2C%22title%22%3A%22%E3%80%90%E6%96%B0%E5%A4%A9%E9%BE%99%E5%85%AB%E9%83%A8%E3%80%91%E4%BB%A4%E7%89%8C%E5%B1%95%E7%A4%BA%E5%8A%9F%E8%83%BD%E4%B8%8A%E7%BA%BF%E5%95%A6%EF%BC%81%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1427165782000%2C%22context%22%3A%22'TL''ZJ'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%5D","id":20},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":False,"name":"NOTE_UPDATE_TIME","path":"/goods","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"1567694460684","id":21},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":False,"name":"sid","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"b2940e81-9258-4b5b-8c89-055fa48c0664","id":22}]

browser.delete_all_cookies()
for cookie_dict in cookie_list:
    browser.add_cookie(cookie_dict)
browser.get('http://tl.cyg.changyou.com/goods/public')
print('自动登录成功...')

for i in range(1, 400):
    page = 'http://tl.cyg.changyou.com/goods/public?world_id=0&price=1-300&order_by=remaintime&have_chosen=price*1-300&page_num=' + str(
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
            time  = aa.find_element_by_xpath('../../dd[2]/p').text.replace("剩余时间：","")
            if qufu_default in qufu:
                browser.get(url)
                row2 = browser.find_element_by_xpath('//*[@id="goods-detail"]/div/div[4]/div[1]/div/div[6]/span').text
                guanzhu = browser.find_element_by_xpath('//*[@id="btnCollect"]').text
                if guanzhu.strip()=='':
                    browser.get(url)
                    guanzhu = browser.find_element_by_xpath('//*[@id="btnCollect"]').text
                browser.get(page)
                if int(row2) >= 190:
                    print(time +'   '+guanzhu+'   '+price + '  ' + row2 + '   ' + title + '  ' + detail + '  ' + ' ' + qufu + '  ' + str(url))
        except StaleElementReferenceException as e:
            server = browser.find_elements_by_class_name('server-info')
            pass

