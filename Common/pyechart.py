from pyecharts import options
from pyecharts.charts import Line
from pyecharts.globals import _CurrentConfig


class Graphical:
    """创建图形类,注意运行时一定要先运行x_axis_config函数，再运行y_axis_config函数否则会报错
    框架官方文档:https://pyecharts.org/#/zh-cn/intro"""

    def __init__(self):
        """默认填创建对象"""
        self.c = Line()  # 创建图表对象

    def x_axis_config(self, x_data) -> None:
        """写入X轴的数据和一些配置"""
        self.c.add_xaxis(xaxis_data=x_data)

    def y_axis_config(self, y_data, *args, name, **kwargs) -> None:
        if name == "":
            raise Exception("请输入数据名称")
        self.c.add_yaxis(y_axis=y_data, is_connect_nones=True, series_name=name,
                         markpoint_opts=options.MarkPointOpts(  # 设置最大最小值
                             # 标记点的数据
                             data=[
                                 # type标注的最大最小值，name标注的名字
                                 options.MarkPointItem(type_="max", name="最大值"),
                                 options.MarkPointItem(type_="min", name="最小值")]),
                         markline_opts=options.MarkLineOpts(  # 设置平均值
                             data=[options.MarkLineItem(type_="average", name="平均值")]
                         )
                         , *args, **kwargs)

    def CurrentConf(self) -> _CurrentConfig:
        """设置全局变量"""
        CurrentConfig = _CurrentConfig()
        return CurrentConfig

    def set_global(self, title="LOG", *args, **kwargs) -> None:
        """设置全局变量"""
        self.c.set_global_opts(title_opts=options.TitleOpts(title=title),  # 设置title名称
                               tooltip_opts=options.TooltipOpts(trigger="axis"),  # 坐标轴触发 (折线图)
                               toolbox_opts=options.ToolboxOpts(is_show=True),  # 是否显示工具栏组件
                               datazoom_opts=options.DataZoomOpts(range_start=0, range_end=100),
                               # 坐标轴配置 坐标轴类型:类目轴 坐标轴两边留白策略
                               xaxis_opts=options.AxisOpts(type_="category", boundary_gap=False),
                               *args,
                               **kwargs)

    def Html_Storage(self, name="A88Log分析.html") -> None:
        """html文件存储位置不写则默认当前目录下"""
        self.c.render(name)

    def get_pyechart(self):
        """获取pyechart对象"""
        return self.c
