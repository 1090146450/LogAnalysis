# 创建取值的一个类，用来判断列表中是否含有想要的值
import re


class Value_book:
    # 判断列表中是否有CPU的值
    def Cpu_00(self, List_Value):
        # 如果判断的值在列表中则开始添加值,创建的CPU_01是存储一条中所有CPU的数据
        Cpu_01 = []
        if "CPU OCCUPY" in List_Value[self + 2]:
            Cpu_01.append(List_Value[self + 1])
            Cpu_02 = [["Total", "Cpu0", "Cpu1", "Cpu2"],
                      ["Total.(\d+)%.", "Cpu0.(\d+)%.", "Cpu1.(\d+)%.", "Cpu2.(\d+)%."]]
            for x in range(0, 4):
                if Cpu_02[0][x] in List_Value[self + 2]:
                    Cpu_01 += re.findall(Cpu_02[1][x], List_Value[self + 2])
                else:
                    Cpu_01.append("")
            return Cpu_01

    def Fps(self, List_Value):
        Fps_01 = [[], [], [], []]
        Fps_List = ["dms0 RUNNING", "oms1 RUNNING", "oms2 RUNNING", "oms3 RUNNING"]
        Fps_List_name = ["dms0 RUNNING: (.*\d*.*?) fps", "oms1 RUNNING: (.*\d*.*?) fps", "oms2 RUNNING: (.*\d*.*?) fps",
                         "oms3 RUNNING: (.*\d*.*?) fps"]
        for x in range(0, 4):
            if Fps_List[x] in List_Value[self + 2]:
                Fps_01[x].append(List_Value[self + 1])
                if re.findall(Fps_List_name[x], List_Value[self + 2]):
                    Fps_01[x] += re.findall(Fps_List_name[x], List_Value[self + 2])
                else:
                    Fps_01[x].append("")
        return Fps_01

    def Sqi(self, List_Value):
        Sqi_00 = []
        if "DEV ETHNET" in List_Value[self + 2]:
            Sqi_00.append(List_Value[self + 1])
            Sqi_01 = [["sqi_value", "sqi_level"], ["sqi_value\[(\d+\.?\d+?)\]", "sqi_value\[(\d+\.?\d+?)\]"]]
            for x in range(0, 2):
                if Sqi_01[0][x] in List_Value[self + 2]:
                    Sqi_00 += (re.findall(Sqi_01[1][x], List_Value[self + 2]))
                else:
                    Sqi_00.append("")
        return Sqi_00

    def SyS_MEMOPY(self, List_Value):
        MEMOPY_00 = []
        if "SYS MEMORY" in List_Value[self + 2]:
            MEMOPY_00.append(List_Value[self + 1])
            MEMOPY_02 = [["Total", "Free", "Avai", "Cach"],
                         ["Total\[(\d+\.?\d+?)MB\]", "Free\[(\d+\.?\d+?)MB\]", "Avai\[(\d+\.?\d+?)MB\]",
                          "Cach\[(\d+\.?\d+?)MB\]"]]
            for x in range(0, 4):
                if MEMOPY_02[0][x] in List_Value[self + 2]:
                    MEMOPY_00 += re.findall(MEMOPY_02[1][x], List_Value[self + 2])
                else:
                    MEMOPY_00.append("")
            return MEMOPY_00
