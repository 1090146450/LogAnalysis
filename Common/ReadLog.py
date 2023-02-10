import re
from Common.Vlaue_book import Value_book


class readlog:
    """变量解读：
    cup:cpu 占用率
    Fps:fps的占用率 [[Dms时间],[Dms帧率],[oms1时间],[oms1帧率],[oms2时间],[oms2帧率],[oms3时间],[oms3帧率]]分别对应4个摄像头的帧率
    sqi:DEV ETHNET值[[时间][数据]]
    MEMOPY:存储占用 [[时间][数据]]
    注意：如果为空或者没有这个值则返回的是空字符串"""
    Cup, Fps, CAM_VOLTAGES, MEMOPY = [[], [], [], [], [], []], [[], [], [], [], [], [], [], []], \
                                     [[], [], [], [], []], [[], [], [], [], []]

    def __init__(self, file):
        self.file = file

    def Input(self) -> None:
        """读取数据并放入Value_book中处理"""
        with open(self.file, mode="r", errors="ignore") as op:
            while True:
                # 每一行提取出来的数据
                a = op.readline()
                # 判断一行内是否为一条数据防止一行多条数据却取一条的值
                # 根据时间来进行拆分  时间的通配符为：".(\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d)"
                a_time = "(\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d)"
                # 进行拆分成列表
                one_a = re.split(a_time, a)
                # 放入循环中，如果有几条数据则循环几次从而解决一行多条数据却提取一次值
                for i in range(int((len(one_a) - 1) / 2)):
                    # 然后开始判断列表中是否含有想要取出的值
                    # 提前判断这行中是否有想要的数据
                    Cpu00 = Value_book.Cpu_00(i, one_a)
                    Fps_00 = Value_book.Fps(i, one_a)
                    CAM_VOLTAGE = Value_book.CAM_VOLTAGE(i, one_a)
                    MEMOPY_00 = Value_book.SyS_MEMOPY(i, one_a)
                    # 这是第一个表格 如果有数据则添加到列表中  返回值为[]
                    if Cpu00:
                        for i in range(len(Cpu00)):
                            self.Cup[i].append(Cpu00[i])
                    # 这是第二个 因为定义的为列表嵌套，所以就算各个列表为空他也是为1，所以需要判断是否为各个列表为空 返回值为
                    if Fps_00 != [[], [], [], []]:
                        for x in range(len(Fps_00)):
                            if Fps_00[x]:
                                self.Fps[x * 2].append(Fps_00[x][0])
                                self.Fps[x * 2 + 1].append(Fps_00[x][1])
                    #     这是第三个
                    if CAM_VOLTAGE:
                        for i in range(len(CAM_VOLTAGE)):
                            self.CAM_VOLTAGES[i].append(CAM_VOLTAGE[i])
                    # 这是第四个
                    if MEMOPY_00:
                        for i in range(len(MEMOPY_00)):
                            self.MEMOPY[i].append(MEMOPY_00[i])
                if a == "":
                    break
