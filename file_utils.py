import os
import urllib.request
from PIL import Image

file_path = 'D:/test/pic'
file_name = "imgage.jpg"

# @staticmethod
def save_image(url, file_name=file_name, file_path=file_path):
    try:
        # 是否有这个路径
        if not os.path.exists(file_path):
            # 创建路径
            os.makedirs(file_path)
            # 获得图片后缀
        file_suffix = os.path.splitext(url)[1]
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(url, filename=filename)
        return filename
    except Exception as e:
        print("IOError")

if __name__=='__main__':
    aa = save_image('http://tl.cyg.changyou.com/transaction/captcha-image?goods_serial_num=201908111513299821&amp;t=1566112633066')
    print(aa)