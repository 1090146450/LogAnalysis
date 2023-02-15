from pyecharts.charts import Page, Tab

from Common import pyechart
from Common.ReadLog import readlog


class RunLogChart:
    def __init__(self, file):
        """创建多图表对象"""
        self.runlog(file=file)

    def runlog(self, file) -> None:
        rl = readlog(file)  # 创建读取log对象
        rl.Input()  # 获取LOG
        page = Page(page_title="DMS_LOG分析")  # 创建顺序多图对象
        tab = Tab()  # 创建选项卡多图对象
        cpu, fps, cam, memo = rl.Cup, rl.Fps, rl.CAM_VOLTAGES, rl.MEMOPY
        cou_title = ["Total", "Cpu0", "Cpu1", "Cpu2", "Cpu3"]
        if len(memo[0]) == len(memo[1]) == len(memo[2]) == len(memo[3]) == len(memo[4]):
            SYS_MEMORY = pyechart.Graphical()
            SYS_MEMORY.x_axis_config(memo[0])
            SYS_MEMORY.y_axis_config(name="Total(MB)", y_data=memo[1])
            SYS_MEMORY.y_axis_config(name="Free(MB)", y_data=memo[2])
            SYS_MEMORY.y_axis_config(name="Avai(MB)", y_data=memo[3])
            SYS_MEMORY.y_axis_config(name="Cach(MB)", y_data=memo[4])
            SYS_MEMORY.set_global(title="SYS MEMORY")
            page.add(SYS_MEMORY.get_pyechart())
        for i in range(1, len(cpu)):
            if len(cpu[0]) == len(cpu[i]):
                cpu_0 = pyechart.Graphical()
                cpu_0.x_axis_config(cpu[0])
                cpu_0.y_axis_config(name=cou_title[i - 1], y_data=cpu[i])
                cpu_0.set_global(title=cou_title[i - 1])
                tab.add(cpu_0.get_pyechart(), cou_title[i - 1])
        fps_title = ["DMS帧率", "OMS1帧率", "OMS2帧率", "OMS3帧率"]
        for i in range(int(len(fps) / 2)):
            if len(fps[i * 2]) == len(fps[i * 2 + 1]):
                fps_0 = pyechart.Graphical()
                fps_0.x_axis_config(fps[i * 2])
                fps_0.y_axis_config(name=fps_title[i], y_data=fps[i * 2 + 1])
                fps_0.set_global(title=fps_title[i])
                page.add(fps_0.get_pyechart())
        if len(cam[0]) == len(cam[1]) == len(cam[2]) == len(cam[3]) == len(cam[4]):
            cam_0 = pyechart.Graphical()
            cam_0.x_axis_config(cam[0])
            cam_0.y_axis_config(name="DMS0", y_data=cam[1])
            cam_0.y_axis_config(name="OMS1", y_data=cam[2])
            cam_0.y_axis_config(name="OMS2", y_data=cam[3])
            cam_0.y_axis_config(name="OMS3", y_data=cam[4])
            cam_0.set_global(title="CAM VOLTAGE")
            page.add(cam_0.get_pyechart())
        tab.render("cpu.html")
        page.render("list.html")
