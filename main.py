# 像图中添加坐标  向X轴添加数据0,2,6  向Y轴添加数据0,3,100
import numpy
from Common.ReadLog import readlog
import test

rl = readlog()
rl.Input()
e1_x = []
e1_y = []
for i in rl.Fps[0]:
    if i[1]:
        e1_x.append(i[0])
        e1_y.append(int(i[1]) if int(i[1]) < 50 else "")
test.high_temperature = e1_y
test.week_name_list = e1_x
print(e1_y)
test.x(e1_x, e1_y)
