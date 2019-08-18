from selenium import webdriver

cookies = """CYG_TGC=CYG_TGC-1879897-UEcNxP6O9sgro19iDfM9v3OMsQGzg1CnGKn"""

def get_cookies():
    cookies_list = []
    split = cookies.split(';')
    print(len(split))
    for i in split:
        cookies_dict = {}
        kv = i.strip().split("=")
        cookies_dict['name'] = kv[0]
        cookies_dict['value'] = kv[1]
        print(kv[0] + ' ==========' + kv[1])
        cookies_list.append(cookies_dict)
    return cookies_list

def set_cookies(driver):
    cookies_list = get_cookies()
    for i in cookies_list:
        # 4.这里需要先删掉之前那次访问时的同名cookie，不然自己设置的cookie会失效
        driver.delete_cookie(i['name'])
        # 添加自己的cookie
        driver.add_cookie(i)
    return driver

aa =get_cookies();
print(aa)