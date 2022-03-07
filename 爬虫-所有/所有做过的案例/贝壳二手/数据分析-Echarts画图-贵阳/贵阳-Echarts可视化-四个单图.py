import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie, Scatter, Bar, Page

page = Page()
df = pd.read_csv('贵阳处理之后.csv', encoding='utf-8')


def drawPie():
    # 获取数据
    y_data = []
    df1 = df[(df['价格'] >= 0) & (df['价格'] <= 50)]
    y_data.append(len(df1))
    df2 = df[(df['价格'] >= 51) & (df['价格'] <= 100)]
    y_data.append(len(df2))
    df3 = df[(df['价格'] >= 101) & (df['价格'] <= 150)]
    y_data.append(len(df3))
    df4 = df[(df['价格'] >= 151) & (df['价格'] <= 200)]
    y_data.append(len(df4))
    df5 = df[(df['价格'] >= 201)]
    y_data.append(len(df5))
    # 饼图
    x_data = ["0-50W", "51W-100W", "101W-150W", "151W-200W", "大于200W"]
    pie = (
        Pie()
            .add("", [list(z) for z in zip(x_data, y_data)])
            .set_global_opts(title_opts=opts.TitleOpts(title="贵阳房价价格区间统计"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render("贵阳房价价格区间统计-饼图.html")
    )
    return pie


# 柱状图
def drawBar():
    df3 = df['房屋朝向'].value_counts()[:8]
    areaX = df['房屋朝向'].value_counts().index.tolist()[:8]
    areaY = []
    for i in df3:
        areaY.append(i)
    # 柱状图
    bar = Bar()
    bar.add_xaxis(areaX)
    bar.add_yaxis("房屋朝向统计", areaY)
    bar.render("房屋朝向统计-柱状图.html")


# 折线图

def drawLine():
    df2 = df['小区'].value_counts()  # 获取折线图数据
    name = df['小区'].value_counts().index.tolist()
    data = []
    for i in df2:
        data.append(i)
    x_data = name[0:5]
    y_data = data[0:5]
    print(x_data)
    from pyecharts.charts import Line

    c = (
        Line()
            .add_xaxis(x_data)
            .add_yaxis("小区房源数量统计", y_data)
            .set_global_opts(title_opts=opts.TitleOpts(title="前五小区房源数折线图"))
            .render("小区房源数量统计-折线图.html")
    )
    return c


# 散点图
def drawScatter():
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
    c = (
        Scatter()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_series_opts()
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="一百个数据面积价格散点图",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
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
            .render("面积价格散点图-散点图.html")
    )
    return c


if __name__ == '__main__':
    drawScatter()
    drawLine()
    drawBar()
    drawPie()
