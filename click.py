from pymouse import *
import time

m = PyMouse()
time.sleep(3)
(x, y) = m.position()  # 获取当前坐标的位置
print(x, y)
m.move(x, y)  # 鼠标移动到(x,y)位置
for num in range(100):
    print(num)
    m.click(x, y)
    time.sleep(0.5)
