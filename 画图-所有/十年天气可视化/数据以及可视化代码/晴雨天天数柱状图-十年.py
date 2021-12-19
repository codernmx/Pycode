import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Page
from pyecharts.faker import Faker


def drawBar(year, data_x, data_y):
    c = (
        Bar()
            .add_xaxis(['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'])
            .add_yaxis("晴天", data_x)
            .add_yaxis("雨天", data_y)
            .set_global_opts(title_opts=opts.TitleOpts(title=year + "年晴雨天天数柱状图"))
        # .render("bar_base.html")
    )
    return c


def StatisticOneYear(OneYearData):
    label = ['晴', '雨']
    # print(OneYearData)
    valCount = {
        "01": {
            "qin": 0,
            "yu": 0,
        },
        "02": {
            "qin": 0,
            "yu": 0,
        },
        "03": {
            "qin": 0,
            "yu": 0,
        },
        "04": {
            "qin": 0,
            "yu": 0,
        },
        "05": {
            "qin": 0,
            "yu": 0,
        },
        "06": {
            "qin": 0,
            "yu": 0,
        },
        "07": {
            "qin": 0,
            "yu": 0,
        },
        "08": {
            "qin": 0,
            "yu": 0,
        },
        "09": {
            "qin": 0,
            "yu": 0,
        },
        "10": {
            "qin": 0,
            "yu": 0,
        },
        "11": {
            "qin": 0,
            "yu": 0,
        },
        "12": {
            "qin": 0,
            "yu": 0,
        }
    }
    for index, row in OneYearData.iterrows():
        data = str(row["日期"])
        cutStr = str(row["天气状况"])
        one = cutStr.split('/')[0]  # 白天
        if ('-01-' in data) and one == '晴':
            valCount['01']['qin'] += 1
        elif ('-01-' in data) and '雨' in one:
            valCount['01']['yu'] += 1

        elif ('-02-' in data) and one == '晴':
            valCount['02']['qin'] += 1
        elif ('-02-' in data) and '雨' in one:
            valCount['02']['yu'] += 1

        elif ('-03-' in data) and one == '晴':
            valCount['03']['qin'] += 1
        elif ('-03-' in data) and '雨' in one:
            valCount['03']['yu'] += 1

        elif ('-04-' in data) and one == '晴':
            valCount['04']['qin'] += 1
        elif ('-04-' in data) and '雨' in one:
            valCount['04']['yu'] += 1

        elif ('-05-' in data) and one == '晴':
            valCount['05']['qin'] += 1
        elif ('-05-' in data) and '雨' in one:
            valCount['05']['yu'] += 1

        elif ('-06-' in data) and one == '晴':
            valCount['06']['qin'] += 1
        elif ('-06-' in data) and '雨' in one:
            valCount['06']['yu'] += 1

        elif ('-07-' in data) and one == '晴':
            valCount['07']['qin'] += 1
        elif ('-07-' in data) and '雨' in one:
            valCount['07']['yu'] += 1

        elif ('-08-' in data) and one == '晴':
            valCount['08']['qin'] += 1
        elif ('-08' in data) and '雨' in one:
            valCount['08']['yu'] += 1

        elif ('-09-' in data) and one == '晴':
            valCount['09']['qin'] += 1
        elif ('-09-' in data) and '雨' in one:
            valCount['09']['yu'] += 1

        elif ('-10-' in data) and one == '晴':
            valCount['10']['qin'] += 1
        elif ('-10-' in data) and '雨' in one:
            valCount['10']['yu'] += 1

        elif ('-11-' in data) and one == '晴':
            valCount['11']['qin'] += 1
        elif ('-11-' in data) and '雨' in one:
            valCount['11']['yu'] += 1

        elif ('-12-' in data) and one == '晴':
            valCount['12']['qin'] += 1
        elif ('-12-' in data) and '雨' in one:
            valCount['12']['yu'] += 1

    return valCount


if __name__ == '__main__':
    FJWeatherData = pd.ExcelFile(r'福州天气爬虫.xlsx')  # 读取天气数据
    # 数据按年份分了sheet存储,每次提取一个sheet即可
    SheetNames = FJWeatherData.sheet_names  # 获取福州天气爬虫工作区的工作表名称，一年一个工作区  #获取所有sheet
    print(SheetNames)
    info = {}
    for i in SheetNames:  # i为年份
        OneYearData = pd.read_excel('福州天气爬虫.xlsx', sheet_name=i)
        OneYearData = OneYearData[['日期', '天气状况']]
        PieData = StatisticOneYear(OneYearData)  # 获得天数统计的list
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        data_x = []
        data_y = []

        for k in month:
            data_x.append(PieData[k]['qin'])
            data_y.append(PieData[k]['yu'])
            info[i] = {
                "data_x": data_x,
                "data_y": data_y,
            }

    print(info)
    def Page_total():
        page = (
            Page(layout=Page.DraggablePageLayout)
                .add(
                drawBar('2011', info['2011']['data_x'], info['2011']['data_y']),
                drawBar('2012', info['2012']['data_x'], info['2012']['data_y']),
                drawBar('2013', info['2013']['data_x'], info['2013']['data_y']),
                drawBar('2014', info['2014']['data_x'], info['2014']['data_y']),
                drawBar('2015', info['2015']['data_x'], info['2015']['data_y']),
                drawBar('2016', info['2016']['data_x'], info['2016']['data_y']),
                drawBar('2017', info['2017']['data_x'], info['2017']['data_y']),
                drawBar('2018', info['2018']['data_x'], info['2018']['data_y']),
                drawBar('2019', info['2019']['data_x'], info['2019']['data_y']),
                drawBar('2020', info['2020']['data_x'], info['2020']['data_y']),
                drawBar('2021', info['2021']['data_x'], info['2021']['data_y']),
            )
        )
        page.render('晴雨天天数柱状图.html')   #渲染页面要自己打开拿到chart_config   然后不要这个渲染  直接下边save 得到最终页面
        # Page.save_resize_html('晴雨天天数柱状图.html', cfg_file='chart_config (3).json', dest='晴雨天天数柱状图-最终.html')


    Page_total()
    os.system('晴雨天天数柱状图-十年.html')
