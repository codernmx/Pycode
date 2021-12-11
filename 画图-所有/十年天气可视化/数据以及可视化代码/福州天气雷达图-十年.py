import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Radar,Page



def drawradar(year):
    df = pd.read_excel('福州天气爬虫.xlsx', sheet_name=year)
    df3 = df['风力风向'].value_counts()
    areaX = df['风力风向'].value_counts().index.tolist()
    areaY = []
    for i in df3:
        areaY.append(i)
    print(areaX)
    print(areaY)
    c_schema = []
    for i in areaX:
        c_schema.append({"name": i, "max": 400, "min": 10},)

    c = (
        Radar()
        .add_schema(schema=c_schema, shape="circle")
        .add("风力等级", [areaY], color="#f9713c")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title=year+"年风力等级雷达图"))
        # .render("radar_air_quality.html")
    )
    return c
def Page_total():
    page = (
        Page(layout=Page.DraggablePageLayout)
            .add(
            drawradar('2011'),
            drawradar('2012'),
            drawradar('2013'),
            drawradar('2014'),
            drawradar('2015'),
            drawradar('2016'),
            drawradar('2017'),
            drawradar('2018'),
            drawradar('2019'),
            drawradar('2020'),
            drawradar('2021'),
        )
    )
    # page.render('雷达图-未配置.html')  # 渲染页面要自己打开拿到chart_config   然后不要这个渲染  直接下边save 得到最终页面
    # Page.save_resize_html('雷达图-未配置.html', cfg_file='chart_config (2).json', dest='雷达图-final.html')


Page_total()
os.system('福州天气雷达图-十年.html')