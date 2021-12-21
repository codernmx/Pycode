import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
import numpy


def StatisticOneYear(OneYearData):
    label = ['晴',  '雨', '阴']
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

    WeatherConditionList = []
    for WeatherConditionName in label:
        WeatherConditionList.append(WeatherConditionDict[WeatherConditionName])
    return WeatherConditionList


def absolute_value(val):
    a = numpy.round(val / 100. * 365, 0)
    return a


if __name__ == '__main__':
    FJWeatherData = pd.ExcelFile(r'福州天气爬虫.xlsx')  # 读取天气数据
    # 数据按年份分了sheet存储,每次提取一个sheet即可
    SheetNames = FJWeatherData.sheet_names  # 获取福州天气爬虫工作区的工作表名称，一年一个工作区
    plt.figure(1)

    label = [u'晴', u'雨', u'阴']
    color = ['green', 'yellow', 'purple']

    k = 1
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    for i in SheetNames:  # i为年份
        OneYearData = pd.read_excel('福州天气爬虫.xlsx', sheet_name = i)
        OneYearData = list(OneYearData['天气状况'])
        PieData = StatisticOneYear(OneYearData)  # 获得天数统计的list
        ax = plt.subplot(4, 3, k)  # 选中子区域
        plt.pie(PieData, labels=label, labeldistance=1, colors=color, startangle=90, shadow=True,
                autopct=absolute_value)
        # 标签存在重叠问题，加入labeldistance参数
        ax.set_title(str(i) + '年天气状况')
        k += 1
        if k == 12:
            break
    plt.show()