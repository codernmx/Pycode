import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Line
from pyecharts.globals import ThemeType


def drawBar(year, data_x):
    list = []
    for i in data_x:
        list.append(round(i / 30))
    print(list)
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            # Line()
            .add_xaxis(['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'])
            .add_yaxis(year + "年每月最高平均温度", list)
            .set_global_opts(title_opts=opts.TitleOpts(title=year + "年每月最高平均温度"))
    )
    return c


def StatisticOneYear(OneYearData):
    valCount = {
        "01": {
            "number": 0,
        },
        "02": {
            "number": 0,
        },
        "03": {
            "number": 0,
        },
        "04": {
            "number": 0,
        },
        "05": {
            "number": 0,
        },
        "06": {
            "number": 0,
        },
        "07": {
            "number": 0,
        },
        "08": {
            "number": 0,
        },
        "09": {
            "number": 0,
        },
        "10": {
            "number": 0,
        },
        "11": {
            "number": 0,
        },
        "12": {
            "number": 0,
        }
    }
    for index, row in OneYearData.iterrows():
        data = str(row["日期"])
        cutStr = str(row["气温"])
        one = cutStr.split('/')[0].split('℃')[0]
        # print(one)
        if ('-01-' in data):
            valCount['01']['number'] += int(one)

        elif ('-02-' in data):
            valCount['02']['number'] += int(one)
        elif ('-03-' in data):
            valCount['03']['number'] += int(one)

        elif ('-04-' in data):
            valCount['04']['number'] += int(one)

        elif ('-05-' in data):
            valCount['05']['number'] += int(one)

        elif ('-06-' in data):
            valCount['06']['number'] += int(one)

        elif ('-07-' in data):
            valCount['07']['number'] += int(one)

        elif ('-08-' in data):
            valCount['08']['number'] += int(one)

        elif ('-09-' in data):
            valCount['09']['number'] += int(one)

        elif ('-10-' in data):
            valCount['10']['number'] += int(one)

        elif ('-11-' in data):
            try:
                valCount['11']['number'] += int(one)
            except:
                valCount['11']['number'] += 0

        elif ('-12-' in data):
            valCount['12']['number'] += int(one)

    return valCount


if __name__ == '__main__':
    FJWeatherData = pd.ExcelFile(r'天气爬虫.xlsx')  # 读取天气数据
    # 数据按年份分了sheet存储,每次提取一个sheet即可
    SheetNames = FJWeatherData.sheet_names  # 获取福州天气爬虫工作区的工作表名称，一年一个工作区  #获取所有sheet
    print(SheetNames)
    info = {}
    for i in SheetNames:  # i为年份
        OneYearData = pd.read_excel('天气爬虫.xlsx', sheet_name=i)
        OneYearData = OneYearData[['日期', '气温']]
        PieData = StatisticOneYear(OneYearData)  # 获得天数统计的list
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        data_x = []

        for k in month:
            data_x.append(PieData[k]['number'])
            info[i] = {
                "data_x": data_x,
            }

    print(info)


    def Page_total():
        page = (
            Page(layout=Page.DraggablePageLayout)
                .add(
                drawBar('2011', info['2011']['data_x']),
                drawBar('2012', info['2012']['data_x']),
                drawBar('2013', info['2013']['data_x']),
                drawBar('2014', info['2014']['data_x']),
                drawBar('2015', info['2015']['data_x']),
                drawBar('2016', info['2016']['data_x']),
                drawBar('2017', info['2017']['data_x']),
                drawBar('2018', info['2018']['data_x']),
                drawBar('2019', info['2019']['data_x']),
                drawBar('2020', info['2020']['data_x']),
                drawBar('2021', info['2021']['data_x']),
            )
        )
        page.render('html/每月最高平均温度.html')  # 渲染页面要自己打开拿到chart_config   然后不要这个渲染  直接下边save 得到最终页面
        Page.save_resize_html('html/每月最高平均温度.html', cfg_file='config/chart_config-3.json', dest='html/每月最高平均温度.html')


    Page_total()
    # os.system('每月最高平均温度.html')
