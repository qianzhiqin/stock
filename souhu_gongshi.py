from selenium import webdriver
# from cookie_utils import set_cookies
import time

from selenium.common.exceptions import StaleElementReferenceException

qufu_default = '纵横双线'
browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.set_script_timeout(30)
browser.get('http://tl.cyg.changyou.com/goods/public')
cookie_list =[{"domain":".changyou.com","expirationDate":1627888779,"hostOnly":False,"httpOnly":False,"name":"_ga","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"GA1.2.532811826.1564816779","id":1},{"domain":".changyou.com","hostOnly":False,"httpOnly":False,"name":"IMGCODE","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"ImageCode-36446-92184dd3-7f49-46a9-ba30-2412d339ba17-NZpNzX","id":2},{"domain":".changyou.com","expirationDate":87964730379,"hostOnly":False,"httpOnly":False,"name":"macid","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"C88BF0C071A00001C96A54661B80DC20","id":3},{"domain":".changyou.com","hostOnly":False,"httpOnly":False,"name":"qrcodeid","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"92d3e4bcd7c7cf530216f68cdc6dfbe02682b99c0f6d4862a9f3c49b1dec431033d96e60fa801f97840e094cd9e8a106","id":4},{"domain":".changyou.com","expirationDate":1582612626,"hostOnly":False,"httpOnly":False,"name":"UM_distinctid","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"16cd1cad26d44e-0154f76c60d44d-e353165-149c48-16cd1cad26e8d9","id":5},{"domain":".cyg.changyou.com","hostOnly":False,"httpOnly":False,"name":"Hm_lpvt_416c770ac83a9d996d7b3793f8c4994d","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"1567168291","id":6},{"domain":".cyg.changyou.com","expirationDate":1598704291,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_416c770ac83a9d996d7b3793f8c4994d","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1567168291","id":7},{"domain":".cyg.changyou.com","expirationDate":1598535500,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1566964859,1566999501","id":8},{"domain":".tl.cyg.changyou.com","hostOnly":False,"httpOnly":False,"name":"Hm_lpvt_416c770ac83a9d996d7b3793f8c4994d","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"1567168305","id":9},{"domain":".tl.cyg.changyou.com","expirationDate":1598704305,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_416c770ac83a9d996d7b3793f8c4994d","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1566999726","id":10},{"domain":".tl.cyg.changyou.com","expirationDate":1598535714,"hostOnly":False,"httpOnly":False,"name":"Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1566961359","id":11},{"domain":"tl.cyg.changyou.com","expirationDate":1658131531,"hostOnly":True,"httpOnly":False,"name":"bdshare_firstime","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"1563437131392","id":12},{"domain":"tl.cyg.changyou.com","expirationDate":1582893105,"hostOnly":True,"httpOnly":False,"name":"CNZZDATA5453193","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"cnzz_eid%3D1025868395-1566884460-http%253A%252F%252Fcyg.changyou.com%252F%26ntime%3D1567163550","id":13},{"domain":"tl.cyg.changyou.com","expirationDate":1598537493.058474,"hostOnly":True,"httpOnly":False,"name":"COOKIE_GOODS_SCANED","path":"/","sameSite":"no_restriction","secure":False,"session":False,"storeId":"0","value":"%25E2%2580%25B2%25E9%2586%2589%25E9%2586%25BA%25E9%2586%25BA%25EF%25BC%258E%25E3%2582%259E%253D201908092130128929%253D488.0%253D2%2527%25E6%2599%259A%25E6%2599%259A%25E5%25B0%258F%25E9%2585%2592%25E5%2590%259E%25EF%25BC%258E%253D201908221949126056%253D380.0%253D4%2527%25E5%25B5%2597%25E6%259C%2588%25E5%25A6%2582%25E6%25AD%258C%25E3%2580%2582%253D201908241825238932%253D350.0%253D8%2527%25EF%25B9%258F%25E4%25B8%25B6%25E4%25BA%258C%25E5%258D%2581%25E5%259B%259B%25E3%2582%259E%253D201908221120420915%253D399.0%253D5%2527%25EF%25B9%258E%25E6%25B8%2585%25E6%25AD%258C%25E7%2595%2599%25E6%25AC%25A2%25C2%25B0%253D20190822356128947%253D500.0%253D8","id":14},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":True,"name":"JSESSIONID","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"BF4215C32150F9E856B6C31230546016","id":15},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":False,"name":"NOTE_CACHE","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"%5B%7B%22id%22%3A200%2C%22title%22%3A%22%E6%B5%8B%E6%9C%8D%E9%BE%99%E9%97%A8NPC%E7%BB%B4%E6%8A%A4%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1432711191000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A198%2C%22title%22%3A%22%E5%AE%A0%E7%88%B1%E4%B8%80%E7%94%9F%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BB%B4%E6%8A%A4%E5%AE%8C%E6%88%90%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1431314942000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A197%2C%22title%22%3A%22%E5%AE%A0%E7%88%B1%E4%B8%80%E7%94%9F%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BB%B4%E6%8A%A4%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1431312451000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A196%2C%22title%22%3A%22%E3%80%904%E6%9C%8817%E6%97%A5%E7%BB%B4%E6%8A%A4%E3%80%91%E7%95%85%E6%98%93%E9%98%81.%E9%81%93%E5%85%B7%E5%9D%8A%E7%BB%B4%E6%8A%A4%E5%85%AC%E5%91%8A%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1429156000000%2C%22context%22%3A%22'TL'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%2C%7B%22id%22%3A192%2C%22title%22%3A%22%E3%80%90%E6%96%B0%E5%A4%A9%E9%BE%99%E5%85%AB%E9%83%A8%E3%80%91%E4%BB%A4%E7%89%8C%E5%B1%95%E7%A4%BA%E5%8A%9F%E8%83%BD%E4%B8%8A%E7%BA%BF%E5%95%A6%EF%BC%81%22%2C%22content%22%3A%22%22%2C%22addTime%22%3A1427165782000%2C%22context%22%3A%22'TL''ZJ'%22%2C%22publishUser%22%3A%22%22%2C%22stick%22%3A0%2C%22stickTime%22%3Anull%2C%22deleteFlag%22%3A0%7D%5D","id":16},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":False,"name":"NOTE_UPDATE_TIME","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"1567168293542","id":17},{"domain":"tl.cyg.changyou.com","hostOnly":True,"httpOnly":False,"name":"sid","path":"/","sameSite":"no_restriction","secure":False,"session":True,"storeId":"0","value":"545f92e5-2bcb-407e-8280-e30a5bd04aa1","id":18}]

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
                if int(row2) >= 250:
                    print(time +'   '+guanzhu+'   '+price + '  ' + row2 + '   ' + title + '  ' + detail + '  ' + ' ' + qufu + '  ' + str(url))
        except StaleElementReferenceException as e:
            server = browser.find_elements_by_class_name('server-info')
            pass

