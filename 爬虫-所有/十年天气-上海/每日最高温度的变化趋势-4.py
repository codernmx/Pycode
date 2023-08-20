import os

import pyecharts.options as opts
from pyecharts.charts import Line, Page
import pandas as pd


def drawLine(year):
    df = pd.read_excel('天气爬虫.xlsx', sheet_name=year)
    oneData = df[['日期']]
    data_xx = []
    for index, row in oneData.iterrows():
        data_xx.append(str(row["日期"]))

    two = df[['气温']]  # 一百个数据的散点图
    data_x = []
    # data_y = [] #低温的
    for index, row in two.iterrows():
        cutStr = str(row["气温"])
        one = cutStr.split('/')[0].split('℃')[0]
        # two_d = cutStr.split('/')[1].split('℃')[0]
        data_x.append(one)
        # data_y.append(two_d)
    print(data_x)
    # print(data_y)
    c = (
        Line()
            .add_xaxis(data_xx)
            .add_yaxis(
            "高温平均气温",
            data_x,
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        #     .add_yaxis(
        #     "低温平均气温",
        #     data_y,
        #     markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        # )  #低温的
            .set_global_opts(title_opts=opts.TitleOpts(title=year + "年每日最高温度的变化趋势"))
        # .render("line.html")
    )
    return c


# os.system('line.html')


def Page_total():
    page = (
        Page(layout=Page.DraggablePageLayout)
            .add(
            drawLine('2011'),
            drawLine('2012'),
            drawLine('2013'),
            drawLine('2014'),
            drawLine('2015'),
            drawLine('2016'),
            drawLine('2017'),
            drawLine('2018'),
            drawLine('2019'),
            drawLine('2020'),
            drawLine('2021'),
        )
    )
    page.render('html/每日最高温度的变化趋势.html')  # 渲染页面要自己打开拿到chart_config   然后不要这个渲染  直接下边save 得到最终页面
    Page.save_resize_html('html/每日最高温度的变化趋势.html', cfg_file='config/chart_config-2.json', dest='html/每日最高温度的变化趋势.html')


Page_total()
# os.system('html/高温低温折线图最终.html')
