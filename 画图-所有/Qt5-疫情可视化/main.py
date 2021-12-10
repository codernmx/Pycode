from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.my_UI()

    def mainH(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./国内疫情可视化/全国现存病例地图.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开

    def deadPeo(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./国内疫情可视化/各地区治愈人数与死亡人数情况.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开

    def deadPeoLv(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./国内疫情可视化/国内各省治愈率与死亡率.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开

    def topFive(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./国内疫情可视化/国内现存病例top-5.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开

    def worLei(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./全球疫情可视化/世界地图-累计死亡.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开

    def worLeiQue(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./全球疫情可视化/世界地图-累计确诊.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开

    def worLeiQueZhi(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./全球疫情可视化/全球各国治愈人数、确诊人数及死亡人数.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开


    def worDeadTopTen(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./全球疫情可视化/死亡人数Top10国家.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开


    def worQueTopTen(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./全球疫情可视化/累计确诊人数Top10国家.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开
    def menuDuiList(self):
        self.setGeometry(200, 200, 1355, 730) #窗口大小
        self.browser = QWebEngineView()# 1 加载html代码
        self.browser.load(QUrl(QFileInfo("./对比可视化/国内外疫情对比.html").absoluteFilePath()))# 读取本地html
        self.setCentralWidget(self.browser) #打开

    def my_UI(self):

        # exitAction.setShortcut('Ctrl+Q')  # 快捷键
        # self.statusBar()  # 创建状态栏，用来显示上面的状态提示


        exitAction = QAction('全国现存病例地图', self)  # QAction菜单栏
        exitAction.triggered.connect(self.mainH)  #绑定点击mainH

        deadPeo = QAction('各地区治愈人数与死亡人数情况', self)  # QAction菜单栏
        deadPeo.triggered.connect(self.deadPeo)  #绑定点击deadPeo

        deadPeoLv = QAction('国内各省治愈率与死亡率', self)  # QAction菜单栏
        deadPeoLv.triggered.connect(self.deadPeoLv)  #绑定点击deadPeoLv


        topFive = QAction('国内现存病例top-5', self)  # QAction菜单栏
        topFive.triggered.connect(self.topFive)  #绑定点击topFive

        worLei = QAction('世界地图-累计死亡', self)  # QAction菜单栏
        worLei.triggered.connect(self.worLei)  #绑定点击topFive

        worLeiQue = QAction('世界地图-累计确诊', self)  # QAction菜单栏
        worLeiQue.triggered.connect(self.worLeiQue)  #绑定点击topFive

        worLeiQueZhi = QAction('全球各国治愈人数、确诊人数及死亡人数', self)  # QAction菜单栏
        worLeiQueZhi.triggered.connect(self.worLeiQueZhi)  #绑定点击topFive

        worDeadTopTen = QAction('死亡人数Top10国家', self)  # QAction菜单栏
        worDeadTopTen.triggered.connect(self.worDeadTopTen)  #绑定点击topFive

        worQueTopTen = QAction('累计确诊人数Top10国家', self)  # QAction菜单栏
        worQueTopTen.triggered.connect(self.worQueTopTen)  #绑定点击topFive

        menuDuiList = QAction('国内外疫情对比', self)  # QAction菜单栏
        menuDuiList.triggered.connect(self.menuDuiList)  #绑定点击topFive




        menubar = self.menuBar()  # menuBar()方法创建了一个菜单栏


        fileMenu = menubar.addMenu('国内疫情可视化')  # 创建一个文件菜单，设置快捷键F

        fileMenu.addAction(exitAction)  # 添加menu下边的东西
        fileMenu.addAction(deadPeo)  # 添加menu下边的各地区治愈人数与死亡人数情况
        fileMenu.addAction(deadPeoLv)  # 添加menu下边的国内各省治愈率与死亡率
        fileMenu.addAction(topFive)  # 添加menu下边的国内各省治愈率与死亡率


        Menu2 = menubar.addMenu('国外疫情可视化')  # 创建一个文件菜单，设置快捷键F
        Menu2.addAction(worLei)
        Menu2.addAction(worLeiQue)
        Menu2.addAction(worLeiQueZhi)
        Menu2.addAction(worDeadTopTen)
        Menu2.addAction(worQueTopTen)
        menuDui = menubar.addMenu('对比可视化')
        menuDui.addAction(menuDuiList)


        self.setGeometry(200, 200, 1355, 730)
        self.setWindowTitle('疫情动态分析')
        self.show()
        self.mainH()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
