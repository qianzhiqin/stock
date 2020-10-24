#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()
result = requests.get("http://fund.eastmoney.com/004745.html", verify=False)
result.encoding = result.apparent_encoding
res = result.text[3:]
soup = BeautifulSoup(res, 'lxml')
stock_zhai = soup.select('div[class="poptableWrap"] table[class="ui-table-hover"]')
for item in stock_zhai:
    for tr in item.contents:
        if len(tr) > 3:
            aaa = tr.s(".alignLeft")
            for td in tr.contents:
                if len(td.string) > 3:
                    aaa = td.select(".alignLeft")

