from pyecharts.charts import Page

from Common import pyechart
from Common.ReadLog import readlog


class RunLogChart:
    def __init__(self, file, name):
        """创建多图表对象"""
        self.page = Page()
        ru = self.runlog(file=file)
        self.page.add(*ru)
        self.page.render(name)

    def runlog(self, file) -> list:
        rl = readlog(file)  # 创建读取log对象
        rl.Input()  # 获取LOG
        axis_list = []
        cpu, fps, cam, memo = rl.Cup, rl.Fps, rl.CAM_VOLTAGES, rl.MEMOPY
        if len(memo[0]) == len(memo[1]) == len(memo[2]) == len(memo[3]) == len(memo[4]):
            SYS_MEMORY = pyechart.Graphical()
            SYS_MEMORY.x_axis_config(memo[0])
            SYS_MEMORY.y_axis_config(name="Total(MB)", y_data=memo[1])
            SYS_MEMORY.y_axis_config(name="Free(MB)", y_data=memo[2])
            SYS_MEMORY.y_axis_config(name="Avai(MB)", y_data=memo[3])
            SYS_MEMORY.y_axis_config(name="Cach(MB)", y_data=memo[4])
            SYS_MEMORY.set_global(title="SYS MEMORY")
            axis_list.append(SYS_MEMORY.get_pyechart())
        if len(cpu[0]) == len(cpu[1]) == len(cpu[2]) == len(cpu[3]) == len(cpu[4]) == len(cpu[5]):
            cpu_0 = pyechart.Graphical()
            cpu_0.x_axis_config(cpu[0])
            cpu_0.y_axis_config(name="Total", y_data=cpu[1])
            cpu_0.y_axis_config(name="Cpu0", y_data=cpu[2])
            cpu_0.y_axis_config(name="Cpu1", y_data=cpu[3])
            cpu_0.y_axis_config(name="Cpu2", y_data=cpu[4])
            cpu_0.y_axis_config(name="Cpu3", y_data=cpu[5])
            cpu_0.set_global(title="CPU占用")
            axis_list.append(cpu_0.get_pyechart())
        fps_title = ["DMS帧率", "OMS1帧率", "OMS2帧率", "OMS3帧率"]
        for i in range(int(len(fps) / 2)):
            if len(fps[i * 2]) == len(fps[i * 2 + 1]):
                fps_0 = pyechart.Graphical()
                fps_0.x_axis_config(fps[i * 2])
                fps_0.y_axis_config(name=fps_title[i], y_data=fps[i * 2 + 1])
                fps_0.set_global(title=fps_title[i])
                axis_list.append(fps_0.get_pyechart())
        print(axis_list)
        return axis_list


rn = RunLogChart("D:/02_Program/Log_Analysis/invo-log.txt", "A88分析.html")
