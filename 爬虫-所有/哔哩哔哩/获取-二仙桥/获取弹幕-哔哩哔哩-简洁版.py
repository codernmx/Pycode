import re
import time
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Origin': 'https://www.bilibili.com',
    'Connection': 'keep-alive',
    'TE': 'Trailers'
}
videoList = []
step = 0
danmuList = ''
chartTitle = ''

def printCharts(detail, list):
    # 添加图形属性
    plt.xlabel('时间段')
    plt.ylabel('弹幕数量')
    title = '' + '各个时段弹幕数量'
    plt.title(title)
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.ylim = (10, 40000)

    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的刻度间隔设置为1，并存在变量里
    info = []
    X = []
    Y = []
    for i in range(0, 24):
        Y.append(0)
        X.append(i)
    for item in list:
        timeArray = time.strptime(item['评论时间'], "%Y-%m-%d %H:%M:%S")
        Y[timeArray.tm_hour] += 1
    for a, b, i in zip(X, Y, range(len(X))):  # zip 函数
        plt.text(a, b + 1, "%.f" % Y[i], ha='center', fontsize=10)  # plt.text 函数
    # 这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！
    plt.bar(X, Y, facecolor='red', width=0.5, label='FG-NET')
    plt.legend()
    plt.show()

def printLineChart(information, list):
    # 添加图形属性
    plt.xlabel('时间段')
    plt.ylabel('弹幕数量')
    title = '' + '各个时段弹幕数量'
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.title(title)
    plt.ylim = (10, 40000)
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的刻度间隔设置为1，并存在变量里
    X = []
    Y = []
    maxTime = 0
    for item in list:
        itemTime = round(round(item['出现时间']) / 60)
        if itemTime > maxTime:
            maxTime = itemTime
    print(maxTime)
    for i in range(0, maxTime + 1):
        Y.append(0)
        X.append(i)
    for item in list:
        itemTime = round(round(item['出现时间']) / 60)
        Y[itemTime] += 1
    for a, b, i in zip(X, Y, range(len(X))):  # zip 函数
        plt.text(a, b + 1, "%.f" % Y[i], ha='center', fontsize=10)  # plt.text 函数
    # 这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！
    plt.plot(Y, color='b', linewidth=0.5, linestyle='-', label='数据三')  # linestyle指定线
    plt.legend()
    plt.show()

def parse_dm(text):
    # 解析视频弹幕    # 输入：视频弹幕的原数据    # 输出：弹幕的解析结果
    result = []  # 用于存储解析结果
    data = re.findall('<d p="(.*?)">(.*?)</d>', text)
    for d in data:
        item = {}  # 每条弹幕数据
        dm = d[0].split(',')  # 弹幕的相关详细，如出现时间，用户等
        item['出现时间'] = float(dm[0])
        item['模式'] = int(dm[1])
        item['字号'] = int(dm[2])
        item['颜色'] = int(dm[3])
        item['评论时间'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(dm[4])))
        item['弹幕池'] = int(dm[5])
        item['用户ID'] = dm[6]  # 并非真实用户ID，而是CRC32检验后的十六进制结果
        item['rowID'] = dm[7]  # 弹幕在数据库中的ID，用于“历史弹幕”功能
        item['弹幕内容'] = d[1]
        result.append(item)
    return result


def getExcelInfo(bvid):
    print(bvid)
    oid = get_cid(bvid)
    url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + str(oid)
    res = requests.get(url)
    res.encoding = 'utf-8'
    text = res.text
    dms = parse_dm(text)
    for i in dms:
        print(i)
    return dms
def get_info(bvid):
    # 获取视频信息    # 输入：视频的bvid    # 输出：视频的相关信息（视频标题、播放量、弹幕数、上传时间）
    url = 'https://api.bilibili.com/x/web-interface/view/detail?bvid=%s' % bvid
    res = requests.get(url, headers)
    data = res.json()
    title = data['data']['View']['title']  # 视频标题
    dm = data['data']['View']['stat']['danmaku']  # 弹幕数
    info = {}
    info['主题'] = title
    info['弹幕数'] = dm
    info['bvid'] = data['data']['View']['bvid']
    return info
def get_cid(bvid):
    # 通过视频的bvid获得视频的cid# 输入：视频的bvid  # 输出：视频的cid
    url = 'https://api.bilibili.com/x/player/pagelist?bvid=%s&jsonp=jsonp' % bvid
    res = requests.get(url, headers=headers)
    data = res.json()
    return data['data'][0]['cid']

def checkSelectt(bvid):
    global danmuList, chartTitle
    if len(bvid) > 0:
        data = get_info(bvid)
        chartTitle = data['主题']
        danmuList = getExcelInfo(bvid)

if __name__ == "__main__":
    bvid = input('请输入哔哩哔哩视频编号：')
    checkSelectt(bvid)
    printLineChart('', danmuList)
    printCharts(chartTitle, danmuList)
    dms = pd.DataFrame(danmuList)
    dms.to_csv('数据.csv', index=False, encoding='utf_8_sig')
