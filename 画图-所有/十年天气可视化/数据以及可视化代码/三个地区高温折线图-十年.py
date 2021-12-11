import os

import pyecharts.options as opts
from pyecharts.charts import Line, Page
import pandas as pd


def drawLine(year):
    df = pd.read_excel('福州天气爬虫.xlsx', sheet_name=year)
    oneData = df[['日期']]
    data_xx = []
    for index, row in oneData.iterrows():
        data_xx.append(str(row["日期"]))

    # 福州高温
    two = df[['气温']]  # 一百个数据的散点图
    data_x = []
    for index, row in two.iterrows():
        cutStr = str(row["气温"])
        one = cutStr.split('/')[0].split('℃')[0]  # 高温
        data_x.append(one)

    # 南平高温
    dfNan = pd.read_excel('福州天气爬虫.xlsx', sheet_name=year)
    twoNan = dfNan[['气温']]  # 一百个数据的散点图
    data_y = []
    for index, row in twoNan.iterrows():
        cutStrNan = str(row["气温"])
        oneNan = cutStrNan.split('/')[0].split('℃')[0]  # 高温
        data_y.append(oneNan)

    # 宁德高温
    dfNIng = pd.read_excel('宁德天气爬虫.xlsx', sheet_name=year)
    twoNing = dfNIng[['气温']]  # 一百个数据的散点图
    data_z = []
    for index, row in twoNing.iterrows():
        cutStrNing = str(row["气温"])
        oneNing = cutStrNing.split('/')[0].split('℃')[0]  # 高温
        data_z.append(oneNing)
    c = (
        Line()
            .add_xaxis(data_xx)
            .add_yaxis(
            "福州天气",
            data_x,
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
            .add_yaxis(
            "南平天气",
            data_y,
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
            .add_yaxis(
            "宁德天气",
            data_z,
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title=year + "三个地区高温折线图"))
        # .render("三个地区高温折线图.html")
    )
    print(data_x,data_y,data_z)
    return c


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
    # page.render('三个地区高温折线图-config.html')  # 渲染页面要自己打开拿到chart_config   然后不要这个渲染  直接下边save 得到最终页面
    # Page.save_resize_html('三个地区高温折线图-config.html', cfg_file='chart_config.json', dest='三个地区高温折线图-最终.html')


Page_total()
os.system('三个地区高温折线图-十年.html')
