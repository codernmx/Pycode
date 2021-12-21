import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Page


def StatisticOneYear(OneYearData):
    label = ['晴', '阴', '雨', '雪']
    WeatherConditionDict = {}
    AllWeatherConditionDict = {}

    for WeatherConditionName in label:
        WeatherConditionDict[WeatherConditionName] = 0

    for OneDayData in OneYearData:
        DayData = OneDayData.split('/')[0]  # 拆分天气，只保留左边，即白天
        if DayData in AllWeatherConditionDict:
            AllWeatherConditionDict[DayData] += 1
        else:
            AllWeatherConditionDict[DayData] = 1

    for WeatherConditionName in AllWeatherConditionDict:
        if WeatherConditionName == '晴':
            WeatherConditionDict['晴'] += AllWeatherConditionDict[WeatherConditionName]
        elif '雨' in WeatherConditionName:
            WeatherConditionDict['雨'] += AllWeatherConditionDict[WeatherConditionName]
        elif WeatherConditionName == '阴':
            WeatherConditionDict['阴'] += AllWeatherConditionDict[WeatherConditionName]
        elif '雪' in WeatherConditionName:
            WeatherConditionDict['雪'] += AllWeatherConditionDict[WeatherConditionName]

    WeatherConditionList = []
    for WeatherConditionName in label:
        WeatherConditionList.append(WeatherConditionDict[WeatherConditionName])
    return WeatherConditionList


def drawPie(year, PieData):
    x_data = [u'晴', u'阴', u'雨', '雪']
    c = (
        Pie()
            .add("", [list(z) for z in zip(x_data, PieData)])
            .set_global_opts(title_opts=opts.TitleOpts(title=year + "年晴-阴-雨-雪的概率"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
        # .render("pie_base.html")
    )
    return c


if __name__ == '__main__':
    FJWeatherData = pd.ExcelFile(r'天气爬虫.xlsx')  # 读取天气数据
    # 数据按年份分了sheet存储,每次提取一个sheet即可
    SheetNames = FJWeatherData.sheet_names  # 获取福州天气爬虫工作区的工作表名称，一年一个工作区
    info = {}
    for i in SheetNames:  # i为年份
        OneYearData = pd.read_excel('天气爬虫.xlsx', sheet_name=i)
        OneYearData = list(OneYearData['天气状况'])
        PieData = StatisticOneYear(OneYearData)  # 获得天数统计的list
        print(PieData)
        info[i] = PieData
    print(info)


    def Page_total():
        page = (
            Page(layout=Page.DraggablePageLayout)
                .add(
                drawPie('2011', info['2011']),
                drawPie('2012', info['2012']),
                drawPie('2013', info['2013']),
                drawPie('2014', info['2014']),
                drawPie('2015', info['2015']),
                drawPie('2016', info['2016']),
                drawPie('2017', info['2017']),
                drawPie('2018', info['2018']),
                drawPie('2019', info['2019']),
                drawPie('2020', info['2020']),
                drawPie('2021', info['2021']),
            )
        )
        page.render('html/晴-阴-雨-雪的概率.html')  # 渲染页面要自己打开拿到chart_config   然后不要这个渲染  直接下边save 得到最终页面
        Page.save_resize_html('html/晴-阴-雨-雪的概率.html', cfg_file='config/chart_config-1.json',
                              dest='html/晴-阴-雨-雪的概率.html')


    Page_total()
    # os.system('html/饼图最终.html')
