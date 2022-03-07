import os
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line, Pie, Bar, Page, Scatter
from pyecharts.globals import ThemeType
# 读取文件
df = pd.read_csv('北京处理之后.csv', encoding='utf-8')


def drawPie():
    # 获取数据
    y_data = []
    df1 = df[(df['价格'] >= 0) & (df['价格'] <= 200)]
    y_data.append(len(df1))
    df2 = df[(df['价格'] >= 201) & (df['价格'] <= 400)]
    y_data.append(len(df2))
    df3 = df[(df['价格'] >= 401) & (df['价格'] <= 600)]
    y_data.append(len(df3))
    df4 = df[(df['价格'] >= 601) & (df['价格'] <= 800)]
    y_data.append(len(df4))
    df5 = df[(df['价格'] >= 801)]
    y_data.append(len(df5))
    # 饼图
    x_data = ["0-200W", "201W-400W", "401W-600W", "601W-800W", "大于800W"]

    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", [list(z) for z in zip(x_data, y_data)])
            .set_global_opts(title_opts=opts.TitleOpts(title="北京房价区间统计"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    return pie


# 柱状图数据
def drawBar():
    # 获取数据
    df3 = df['房屋朝向'].value_counts()[:8]
    areaX = df['房屋朝向'].value_counts().index.tolist()[:8]
    areaY = []
    for i in df3:
        areaY.append(i)
    # 柱状图
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .set_global_opts(title_opts=opts.TitleOpts(title="房屋朝向统计图"))
            .add_xaxis(areaX)
            .add_yaxis("房屋朝向", areaY)
    )
    return bar


# 折线图
def drawZheLine():
    # 获取折线图数据
    df2 = df['小区'].value_counts()
    name = df['小区'].value_counts().index.tolist()
    data = []
    for i in df2:
        data.append(i)
    x_data = name[0:5]
    y_data = data[0:5]
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            # Line()
            .add_xaxis(x_data)
            .add_yaxis("小区房源数量统计", y_data)
            .set_global_opts(title_opts=opts.TitleOpts(title="前五小区房源数折线图"))
    )
    return c


# 散点图
def drawScatter():
    # 获取数据
    two = df[['面积', '价格']].head(100)  # 一百个数据的散点图
    data = []
    for index, row in two.iterrows():
        print(row["面积"], row["价格"])
        one = row["面积"]
        two = row["价格"]
        data.append([one, two])
    data.sort(key=lambda x: x[0])
    x_data = [d[0] for d in data]
    y_data = [d[1] for d in data]
    scatter = (
        Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_series_opts()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="一百个面积-价格散点图"),
            legend_opts=opts.LegendOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(
                type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
        )
    )
    return scatter
def Page_total():
    page = (
        Page(layout=Page.DraggablePageLayout)
            .add(
            drawPie(),
            drawBar(),
            drawZheLine(),
            drawScatter(),
        )
    )
    # page.render('page.html')   #渲染页面要自己打开拿到chart_config   然后不要这个渲染  直接下边save 得到最终页面
    # Page.save_resize_html('page.html', cfg_file='chart_config.json', dest='final.html')
Page_total()
os.system('北京-汇总大屏.html')
