from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '17034281'
API_KEY = 'vNHmu6zHd2j1Rnr3SLREt21e'
SECRET_KEY = 'Sdzsx7FXGTGGswPe41vi7OHjvBKhCGZa'
""" 你的 APPID AK SK end"""

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('C:\\Users\\qianzhiqin\\Desktop\\ImageCode.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
aa = client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
bb = client.basicGeneral(image, options)
print(bb)


""" 调用通用文字识别（高精度版） """
cc = client.basicAccurate(image);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
dd = client.basicAccurate(image, options)
print(dd)
