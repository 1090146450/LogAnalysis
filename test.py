import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker


def x(week_name_list, high_temperature):
    c = (
        # 初始化配置对象
        Line()
            # 向X轴添加数据
            .add_xaxis(xaxis_data=week_name_list)
            # Y轴的配置
            .add_yaxis(
            # 添加标题
            series_name="帧率变化",
            # 添加Y轴数据
            y_axis=high_temperature,
            # 标点配置文件
            markpoint_opts=opts.MarkPointOpts(
                # 标记点的数据
                data=[
                    # type标注的最大最小值，name标注的名字
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            # 再次添加标点配置文件
            markline_opts=opts.MarkLineOpts(
                # 添加平均值
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )
            # 设置全局变量
            .set_global_opts(
            # 设置title配置   title文本内容  副标题文本内容
            title_opts=opts.TitleOpts(title="未来一周气温变化", subtitle="纯属虚构"),
            # 坐标轴触发 (折线图)
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            # 是否显示工具栏组件
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            # 坐标轴配置 坐标轴类型:类目轴 坐标轴两边留白策略
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
            .render("temperature_change_line_chart.html")
    )
