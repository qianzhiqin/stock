import tushare as ts
import os
import pandas as pd

path = os.getcwd() + '/data/list.csv'


def get_stock_list():
    pro = ts.pro_api('9e62fd9e89da705417854591ee4700cbd66cbc2a2ca328dbe1630310')
    # path = os.getcwd() + '/data/list.csv'
    # 查询当前所有正常上市交易的股票列表
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data.to_csv(path, index=True, header=True)


def industry_group():
    data = pd.read_csv(path)
    groupby = data.groupby('industry')
    for name, aaa in groupby:
        print(name)
        # print(aaa)
    # print(groupby)


industry_group()
