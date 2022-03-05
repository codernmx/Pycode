import os

import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie, Scatter, Bar, Page, Radar,Grid

page = Page()
df = pd.read_csv('df.csv', encoding='utf-8')


def drawPie(name):
    df1 = df[name].value_counts()[:8]
    dataX = df[name].value_counts().index.tolist()[:8]
    dataY = []
    for i in df1:
        dataY.append(i)
    pie = (
        Pie()
            .add("", [list(z) for z in zip(dataX, dataY)])
            .set_global_opts(title_opts=opts.TitleOpts(title=str(name)))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render(str(name) + "-饼图.html")
    )
    return pie


# 柱状图
def drawBar():
    df3 = df['工作地点'].value_counts()[:15]
    areaX = df['工作地点'].value_counts().index.tolist()[:15]
    areaY = []
    for i in df3:
        areaY.append(i)
    # 柱状图
    bar = Bar()
    bar.add_xaxis(areaX)
    bar.add_yaxis("工作地点统计", areaY)
    bar.render("工作地点-柱状图.html")


# 折线图

def drawLine():
    df2 = df['学历要求'].value_counts()  # 获取折线图数据
    name = df['学历要求'].value_counts().index.tolist()
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
            .add_yaxis("学历要求统计", y_data)
            .set_global_opts(title_opts=opts.TitleOpts(title="学历要求折线图"))
            .render("学历要求-折线图.html")
    )
    return c




# 散点图
def drawScatter():
    two = df[['最低月薪千', '最高月薪千']].head(500)  # 一百个数据的散点图
    data = []
    for index, row in two.iterrows():
        one = int(row["最低月薪千"])
        two = int(row["最高月薪千"])
        data.append([one, two])
    data.sort(key=lambda x: x[0])
    x_data = [d[0] for d in data]
    y_data = [d[1] for d in data]
    print(data)
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
            title_opts=opts.TitleOpts(title="最高最低月薪-散点图"),
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
            .render("最高最低月薪-散点图.html")
    )
    return c


def drawRadar():
    df5 = df['城市'].value_counts()  # 获取折线图数据
    name = df['城市'].value_counts().index.tolist()
    data = []
    for i in df5:
        data.append(i)
    c_schema = []
    for i in name:
        c_schema.append({
            "name": i
        })
    c = (
        Radar()
            .add_schema(schema=c_schema, shape="circle")
            .add("城市-发布招聘信息数量", [data], color="red")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .render("城市-发布招聘信息数量-雷达图.html")
    )


def drawXlXz():
    df7 = df.groupby('学历要求').mean()
    x_data = []
    y_data = []
    for index, row in df7.iterrows():
        print(index)
        x_data.append(index)
        y_data.append(row['平均月薪千'])
    from pyecharts.charts import Line

    c = (
        Line()
            .add_xaxis(x_data)
            .add_yaxis("学历-平均月薪千", y_data)
            .set_global_opts(title_opts=opts.TitleOpts(title="学历-平均月薪千"))
            .render("学历-薪资-折线图.html")
    )
    return c

if __name__ == '__main__':
    drawXlXz()
    drawScatter()
    drawLine()
    drawBar()
    drawPie('公司性质')
    drawPie('工作经验')
    drawPie('公司规模')
    drawPie('行业')
    drawRadar()

    # 下边是直接浏览器打卡
    os.system('城市-发布招聘信息数量-雷达图.html')
    os.system('最高最低月薪-散点图.html')
    os.system('学历要求-折线图.html')
    os.system('工作地点-柱状图.html')
    os.system('公司性质-饼图.html')
    os.system('工作经验-饼图.html')
    os.system('行业-饼图.html')
    os.system('公司规模-饼图.html')
    os.system('学历-薪资-折线图.html')
