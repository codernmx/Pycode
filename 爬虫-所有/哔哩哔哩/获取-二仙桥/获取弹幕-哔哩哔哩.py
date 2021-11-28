import re
import time
import tkinter

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

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
    '''
    解析视频弹幕
    输入：视频弹幕的原数据
    输出：弹幕的解析结果
    '''
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


def toExcel(bvid):
    print(bvid)
    oid = get_cid(bvid)
    url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + str(oid)
    res = requests.get(url)
    res.encoding = 'utf-8'
    text = res.text
    dms = parse_dm(text)
    return dms


def get_info(bvid):
    '''
    获取视频信息
    输入：视频的bvid
    输出：视频的相关信息（视频标题、播放量、弹幕数、上传时间）
    '''
    url = 'https://api.bilibili.com/x/web-interface/view/detail?bvid=%s' % bvid
    res = requests.get(url, headers)
    data = res.json()
    # print(data['data']['View'])
    title = data['data']['View']['title']  # 视频标题
    view = data['data']['View']['stat']['view']  # 播放量
    dm = data['data']['View']['stat']['danmaku']  # 弹幕数
    upload = time.strftime('%Y-%m-%d', time.localtime(data['data']['View']['pubdate']))  # 上传日期
    # info = [title, view, dm, upload]
    info = {}
    info['主题'] = title
    info['弹幕数'] = dm
    # info['view'] = view
    # info['upload'] = upload
    info['bvid'] = data['data']['View']['bvid']
    return info


def get_cid(bvid):
    '''
    通过视频的bvid获得视频的cid
    输入：视频的bvid
    输出：视频的cid
    '''
    url = 'https://api.bilibili.com/x/player/pagelist?bvid=%s&jsonp=jsonp' % bvid
    res = requests.get(url, headers=headers)
    data = res.json()
    return data['data'][0]['cid']


class Ui_B(object):
    def setupUi(self, B):
        B.setObjectName("B")
        B.resize(1113, 808)
        self.search = QtWidgets.QPushButton(B)
        self.search.setGeometry(QtCore.QRect(890, 70, 161, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.keywords = QtWidgets.QLineEdit(B)
        self.keywords.setGeometry(QtCore.QRect(330, 70, 551, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.keywords.setFont(font)
        self.keywords.setObjectName("keywords")
        self.label = QtWidgets.QLabel(B)
        self.label.setGeometry(QtCore.QRect(70, 70, 261, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(B)
        self.comboBox.setGeometry(QtCore.QRect(190, 150, 691, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.location = QtWidgets.QLineEdit(B)
        self.location.setGeometry(QtCore.QRect(70, 380, 771, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.location.setFont(font)
        self.location.setText("D:/1.csv")
        self.location.setObjectName("location")
        self.fileLocal = QtWidgets.QPushButton(B)
        self.fileLocal.setGeometry(QtCore.QRect(850, 380, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.fileLocal.setFont(font)
        self.fileLocal.setObjectName("fileLocal")
        self.damuList = QtWidgets.QListView(B)
        self.damuList.setGeometry(QtCore.QRect(70, 450, 491, 301))
        self.damuList.setObjectName("damuList")
        self.label_3 = QtWidgets.QLabel(B)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.photo = QtWidgets.QGraphicsView(B)
        self.photo.setGeometry(QtCore.QRect(580, 450, 471, 301))
        self.photo.setObjectName("photo")
        self.pushButton = QtWidgets.QPushButton(B)
        self.pushButton.setGeometry(QtCore.QRect(890, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.barchart = QtWidgets.QPushButton(B)
        self.barchart.setGeometry(QtCore.QRect(570, 320, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.barchart.setFont(font)
        self.barchart.setObjectName("barchart")
        self.lineChart = QtWidgets.QPushButton(B)
        self.lineChart.setGeometry(QtCore.QRect(360, 320, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.lineChart.setFont(font)
        self.lineChart.setObjectName("lineChart")
        self.label_4 = QtWidgets.QLabel(B)
        self.label_4.setGeometry(QtCore.QRect(70, 250, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.keywords_2 = QtWidgets.QLineEdit(B)
        self.keywords_2.setGeometry(QtCore.QRect(240, 250, 641, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.keywords_2.setFont(font)
        self.keywords_2.setObjectName("keywords_2")
        self.pushButton_2 = QtWidgets.QPushButton(B)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(B)
        QtCore.QMetaObject.connectSlotsByName(B)
        self.search.clicked.connect(self.getVideo)
        self.pushButton.clicked.connect(self.checkSelect)
        self.pushButton_2.clicked.connect(self.checkSelectt)
        self.barchart.clicked.connect(self.printChart)
        self.lineChart.clicked.connect(self.printLineCharts)
        self.fileLocal.clicked.connect(self.checkDocumentPath)

    def retranslateUi(self, B):
        _translate = QtCore.QCoreApplication.translate
        B.setWindowTitle(_translate("B", "Dialog"))
        self.search.setText(_translate("B", "搜索"))
        self.label.setText(_translate("B", "输入搜索视频关键词"))
        self.fileLocal.setText(_translate("B", "Excel存储位置"))
        self.label_3.setText(_translate("B", "选择视频"))
        self.pushButton.setText(_translate("B", "确定"))
        self.barchart.setText(_translate("B", "查看柱状图"))
        self.lineChart.setText(_translate("B", "查看折线图"))
        self.label_4.setText(_translate("B", "输入视频bvid"))
        self.pushButton_2.setText(_translate("B", "确定"))

    def getVideo(self):
        search = self.keywords.text()
        for i in range(1, 3):
            Url = 'https://search.bilibili.com/all?keyword=' + search + '&from_source=webtop_search&spm_id_from=333.788&page=' + str(
                i)
            response = requests.get(Url, headers=headers).text
            soup = BeautifulSoup(response, 'html.parser')
            video = soup.select('.img-anchor')
            for item in video:
                tem = item['href'][25: 37]
                videoList.append(tem)
            time.sleep(1)
        comBoxLIst = []
        for item in videoList:
            comBoxLIst.append(str(get_info(item)))
        self.comboBox.addItems(comBoxLIst)

    def checkSelect(self):
        global danmuList, chartTitle
        bvid = ''
        oid = self.comboBox.currentText()
        if len(oid) > 0:
            dist = eval(oid)
            chartTitle = dist['主题']
            bvid = dist['bvid']
            danmuList = toExcel(bvid)
        messagebox.showinfo("完成", "图表渲染完成")


    def checkSelectt(self):
        global danmuList, chartTitle
        bvid = self.keywords_2.text()
        print(bvid)
        if len(bvid) > 0:
            data = get_info(bvid)
            chartTitle = data['主题']
            danmuList = toExcel(bvid)

        messagebox.showinfo("完成", "图表渲染完成")

    def printLineCharts(self):
        if len(danmuList) > 0:
            printLineChart('', danmuList)

    def printChart(self):
        if len(danmuList) > 0:
            printCharts(chartTitle, danmuList)

    def checkDocumentPath(self):
        path = self.location.text()
        if len(path) > 0:
            dms = pd.DataFrame(danmuList)
            dms.to_csv(path, index=False, encoding='utf_8_sig')
            messagebox.showinfo("完成", "存储成功")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_B()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
