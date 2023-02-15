# 创建取值的一个类，用来判断列表中是否含有想要的值
import re


class Value_book:
    # 判断列表中是否有CPU的值
    def Cpu_00(self, List_Value):
        # 如果判断的值在列表中则开始添加值,创建的CPU_01是存储一条中所有CPU的数据
        Cpu_01 = []
        data = List_Value[2 * (self + 1)]
        if "CPU OCCUPY" in data:
            Cpu_01.append(List_Value[2 * (self + 1) - 1])
            Cpu_02 = [["Total", "Cpu0", "Cpu1", "Cpu2", "Cpu3"],
                      ["Total.(\d+)%.", "Cpu0.(\d+)%.", "Cpu1.(\d+)%.", "Cpu2.(\d+)%.", "Cpu3.(\d+)%."]]
            for x in range(0, 5):
                if Cpu_02[0][x] in data:
                    Cpu_01 += re.findall(Cpu_02[1][x], data)
                else:
                    Cpu_01.append("")
            return Cpu_01

    def Fps(self, List_Value):
        Fps_01 = [[], [], [], []]
        data = List_Value[2 * (self + 1)]
        Fps_List = ["[dms0 ", "[oms1 ", "[oms2 ", "[oms3 "]
        Fps_List_name = ["dms0.*?(\d*?) fps", "oms1.*?(\d*?) fps", "oms2.*?(\d*?) fps",
                         "oms3.*?(\d*?) fps"]
        for x in range(0, 4):
            if Fps_List[x] in data:
                Fps_01[x].append(List_Value[2 * (self + 1) - 1])
                if re.findall(Fps_List_name[x], data):
                    Fps_01[x] += re.findall(Fps_List_name[x], data)
                else:
                    Fps_01[x].append("")
        return Fps_01

    def CAM_VOLTAGE(self, List_Value):
        CAM_VOLTAGE_00 = []
        data = List_Value[2 * (self + 1)]
        if "CAM VOLTAGE" in data:
            CAM_VOLTAGE_00.append(List_Value[2 * (self + 1) - 1])
            Sqi_01 = [["DMS0", "OMS1", "OMS2", "OMS3"],
                      ["DMS0\[(\d+\.\d+?)\]", "OMS1\[(\d+\.?\d+?)\]", "OMS2\[(\d+\.?\d+?)\]", "OMS3\[(\d+\.?\d+?)\]"]]
            for x in range(0, 4):
                if Sqi_01[0][x] in data:
                    CAM_VOLTAGE_00 += (re.findall(Sqi_01[1][x], data))
                else:
                    CAM_VOLTAGE_00.append("")
        return CAM_VOLTAGE_00

    def SyS_MEMOPY(self, List_Value):
        MEMOPY_00 = []
        data = List_Value[2 * (self + 1)]
        if "SYS MEMORY" in data:
            MEMOPY_00.append(List_Value[2 * (self + 1) - 1])
            MEMOPY_02 = [["Total", "Free", "Avai", "Cach"],
                         ["Total\[(\d+\.?\d+?)MB\]", "Free\[(\d+\.?\d+?)MB\]", "Avai\[(\d+\.?\d+?)MB\]",
                          "Cach\[(\d+\.?\d+?)MB\]"]]
            for x in range(0, 4):
                if MEMOPY_02[0][x] in data:
                    MEMOPY_00 += re.findall(MEMOPY_02[1][x], data)
                else:
                    MEMOPY_00.append("")
            return MEMOPY_00
