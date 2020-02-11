#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import datetime
from prettytable import PrettyTable
from PIL import Image, ImageDraw, ImageFont
from MysqlHelper import *

helper = MysqlHelper('okaiok.com', 'root', 'qq84607952', 'walle')
helper.connect()
base_path = 'D:/test/'

def send_wechat(content):
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
    print("发送微信状态: " + str(result.status_code))

def send_wechat_img(path):
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
    #将图片上传临时素材
    url_upload = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token='+access_token+'&type=image'
    files = {'file': open(path, 'rb')}
    img_res = requests.post(url_upload, files=files)
    if img_res.status_code != 200:
        print('上传临时图片失败')
    else:
        result_json = json.loads(img_res.text)
        if result_json['errcode'] != 0:
            print('上传临时图片响应结果不正确')
        else:
            media_id = result_json['media_id']
            print("上传图片获取media_id成功： " + media_id)

    data_params = {
        "touser": "@all",
        "msgtype": "image",
        "agentid": 2,
        "image" : {
            "media_id" : media_id
        },
        "safe": 0}
    result = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(access_token),
                           data=json.dumps(data_params),verify=False)
    print("发送微信状态: " + str(result.status_code))


def create_table_img(data, img_name, **kwargs):
    '''
        img_name 图片名称 'D:/project/pythonwork/12306/t.png' 或 t.png
        data 表格内容，首行为表头部
        table_title 表格标题
        line_height 底部描述行高
        font 默认字体路径
        default_font_size 默认字体大小
        default_background_color 图片背景底色
        table_top_heght 设置表格顶部留白高度
        table_botton_heght 设置表格顶部留白高度
        describe 底部描述文字
    '''
    space = 20  ## 表格边距
    # 生成图片-------------------------------
    ### 底部描述行高
    if 'line_height' not in kwargs:
        line_height = 4
    else:
        line_height = kwargs['line_height']

    ### 默认字体
    if 'font' not in kwargs:
        kwargs['font'] = None

    ### 默认字体大小
    if 'default_font_size' not in kwargs:
        kwargs['default_font_size'] = 15

    ### 默认表标题字体大小
    if 'table_title_font_size' not in kwargs:
        kwargs['table_title_font_size'] = 22

    ### 图片背景底色
    if 'default_background_color' not in kwargs:
        kwargs['default_background_color'] = (255, 255, 255, 255)

    ### 设置表格顶部留白高度
    if 'table_top_heght' not in kwargs:
        kwargs['table_top_heght'] = kwargs['table_title_font_size'] + space + int(kwargs['table_title_font_size'] / 2)

    ## 底部描述文字
    if 'describe' in kwargs:
        describe_len = len(kwargs['describe'])
    else:
        describe_len = 0

    ### 设置表格底部留白高度
    if 'table_botton_heght' not in kwargs:
        kwargs['table_botton_heght'] = 3*describe_len * kwargs['default_font_size'] + space

    ### 图片后缀
    if 'img_type' not in kwargs:
        kwargs['img_type'] = 'PNG'

    ### 默认字体及字体大小
    font = ImageFont.truetype(kwargs['font'], kwargs['default_font_size'], encoding='utf-8')
    font2 = ImageFont.truetype(kwargs['font'], kwargs['table_title_font_size'], encoding='utf-8')
    ## Image模块创建一个图片对象
    im = Image.new('RGB', (10, 10), kwargs['default_background_color'])
    ## ImageDraw向图片中进行操作，写入文字或者插入线条都可以
    draw = ImageDraw.Draw(im)

    # 创建表格---------------------------------
    tab = PrettyTable(border=True, header=True, header_style='title')
    ## 第一行设置为表头
    tab.field_names = data.pop(0)
    for row in data:
        tab.add_row(row)
    tab_info = str(tab)
    ## 根据插入图片中的文字内容和字体信息，来确定图片的最终大小
    img_size = draw.multiline_textsize(tab_info, font=font)
    img_width = img_size[0] + space * 2
    table_height = img_size[1] + space * 2
    img_height = table_height + kwargs['table_botton_heght'] + kwargs['table_top_heght']
    im_new = im.resize((img_width, img_height))
    del draw
    del im
    draw = ImageDraw.Draw(im_new, 'RGB')
    draw.multiline_text((space, kwargs['table_top_heght']), tab_info + '\n\n', fill=(0, 0, 0), font=font)
    ### 表标题--------------------------
    if 'table_title' in kwargs:
        title_left_padding = (img_width - len(table_title) * kwargs['table_title_font_size']) / 2
        draw.multiline_text((title_left_padding, space), table_title, fill=(17,0,0), font=font2, align = 'center')

    y = table_height + space/2
    ### 表描述--------------------------
    if 'describe' in kwargs:
        y = y + kwargs['default_font_size']
        frist_row = kwargs['describe'].pop(0)
        draw.text((space,y), frist_row, fill=(255,0,0), font=font)
        for describe_row in kwargs['describe']:
            y = y + kwargs['default_font_size'] + line_height
            draw.text((space,y), describe_row, fill=(0,0,0), font=font)
    del draw
    im_new.save(img_name, kwargs['img_type'])
    return True

def get_niuren_stock(date):
    sql = 'SELECT stock,price,proportion,TYPE,a.user,b.success,date FROM stock a JOIN (SELECT USER,success FROM `user`) b ON a.user=b.user WHERE DATE=%s ORDER BY TYPE, success DESC '
    rows = helper.fetchall(sql, [date])
    res = []
    if rows:
        res = list(map(lambda x: list(x),rows))
    return res

def get_niuren_stock_sum(date):
    sql = 'SELECT stock,TYPE,COUNT(1) AS num FROM stock WHERE DATE=%s GROUP BY stock,TYPE HAVING num>1 '
    rows = helper.fetchall(sql, [date])
    res = []
    if rows:
        res = list(map(lambda x: "日期" +date +" 股票:" +x[0] +" " +x[1] +" " +str(x[2])+" 次数",rows))
    return res

if __name__ == "__main__":
    today = datetime.datetime.now().strftime('%Y%m%d')
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    today = '20200207'
    niuren_stock = get_niuren_stock(today)
    niuren_stock_sum = get_niuren_stock_sum(today)
    title_desc = [" 股票 ", "价格", " 买卖比例  ", "买卖类型", "    牛人     ", "牛人战绩百分比",'日期']
    # 将买卖分开
    if len(niuren_stock) > 1:
        type = '买'
        for i in range(len(niuren_stock)):
            type_tmp = niuren_stock[i][3]
            if type_tmp != type:
                niuren_stock.insert(i, ['---', '---', '---', '---', '---', '---', '---'])
                niuren_stock.insert(i, ['', '', '', '', '', '', ''])
                break

    niuren_stock.insert(0,title_desc)
    describe = ["其他信息："]
    if niuren_stock_sum:
        niuren_stock_sum.insert(0, "其他信息：")
        describe = niuren_stock_sum
    table_title = today  + ' 东方财富牛人榜'
    path = base_path + str(timestamp) + ".png"
    result = create_table_img(niuren_stock, path, font='C:\Windows\Fonts\simkai.ttf', describe=describe,
                              table_title=table_title,default_font_size = 14,table_title_font_size=16)
    if result:
        print('图表生成成功')
# chouma_sql = "SELECT *,(price-costdown90 )/(costup90-costdown90) AS abc FROM chouma ORDER BY abc ASC"
# send_wechat_img(path)