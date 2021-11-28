# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5 import QtCore, QtGui, QtWidgets
import image0_rc
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import *
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import time
import sip






class Ui_MainWindow(QDialog,object):
    def __init__(self):
        super().__init__()
        palette1 = QPalette()
        self.setPalette(palette1)
        self.label = QLabel(self)
        self.label.setFixedWidth(600)
        self.label.move(150, 200)
        # 动态显示时间在label上
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 730)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color:rgb(231, 246, 255)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(890, 550, 950, 421))
        self.groupBox.setObjectName("groupBox")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 20, 240, 31))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1500, 60, 500, 99))
        self.label_6.setObjectName("label_6")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(720, 230, 200, 161))
        self.layoutWidget.setObjectName("layoutWidget")


        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 310, 500, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # self.comboBox.setStyleSheet("QComboBox {"
        #                             "combobox-popup: 0;\n"  # 滚动条设置必需
        #                             "border-style:none; "
        #                             "padding-left:40px;  "  # 字体距离左边的距离
        #                             "width:300px; "
        #                             "height:48px; "
        #                             "font-size:24px; "
        #                             "font-family:PingFangSC-Regular,PingFang SC; "
        #                             "font-weight:400; "
        #                             "color:rgba(93,169,255,1);\n"
        #                             "line-height:24px; }\n"
        #
        #                             "QComboBox:drop-down {"  # 选择箭头样式
        #                             "width:40px;  "
        #                             "height:50px; "
        #                             "border: none;  "
        #                             "subcontrol-position: right center; "  # 位置
        #                             "subcontrol-origin: padding;}\n"  # 对齐方式
        #
        #                             "QComboBox:down-arrow {"  # 选择箭头，继承drop-down
        #                             "border: none; "
        #                             "background: transparent; "
        #                             "image: url(\"./ui/image/down.png\");}\n"
        #
        #                             "QComboBox:down-arrow:pressed { image: url(\"./ui/image/up.png\"); }\n"  # 选择箭头
        #
        #                             "QComboBox QAbstractItemView {"  # 下拉选项样式
        #                             "color:black; "
        #                             "background: transparent; "
        #                             "selection-color:rgba(93,169,255,1);"
        #                             "selection-background-color: rgba(255,255,255,1);"
        #                             "}\n"
        #
        #                             "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
        #                             "width: 6px;\n"
        #                             "height: 100px;"
        #                             "background-color: transparent;  }\n"
        #
        #                             "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
        #                             "border-radius: 3px;   "
        #                             "background: rgba(0,0,0,0.1);}\n"
        #
        #                             # "QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"  # 划过滚动条，变化
        #                             # "background: rgb(90, 91, 93);}\n"
        #
        #                             "QComboBox QScrollBar::add-line::vertical{"  # 滚动条上箭头
        #                             "border:none;}"
        #                             "QComboBox QScrollBar::sub-line::vertical{"  # 滚动条下箭头
        #                             "border:none;}"
        #                             "")



        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)

        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)

        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-800, 10, 1471, 991))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/0.png"))
        self.label_8.setObjectName("label_8")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 280, 60, 60))
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_2.setStyleSheet("background-color:rgb(200, 166, 119);\n"
"color: rgb(255,255,255);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 10pt \"AcadEref\";\n"
"border-style: outset;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 580, 75, 23))
        self.pushButton_3.setStyleSheet("background-color:rgb(200, 166, 119);\n"
"color: rgb(255,255,255);  \n"
"border-radius: 30px;  border: 2px groove gray;\n"
"font: 10pt \"AcadEref\";\n"
"border-style: outset;")
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setStyleSheet("QMenuBar{backgroound-color：rgb(217, 243, 255)}")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.pushButton)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ui"))
        self.label_5.setText(_translate("MainWindow", "智能预警系统"))
        self.label_5.setFont(QFont("Roman times", 12, QFont.Bold))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VI_4"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VI_1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "VI_2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "VI_3"))
        # self.comboBox.currentIndexChanged.connect(self.selectionchange_1)

        self.目检台号 = self.comboBox.currentText()

        self.label_2.setText(_translate("MainWindow", "目检型号"))

        self.label_3.setText(_translate("MainWindow", "机 床 号"))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "BML_1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "BML_2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "BML_3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "BML_4"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "BML_5"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "BML_6"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "BML_7"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "BML_8"))
        self.comboBox_3.currentIndexChanged.connect(self.selectionchange_3)

        self.机床号 = self.comboBox_3.currentText()


        self.label_4.setText(_translate("MainWindow", "零件类型"))

        self.pushButton.setText(_translate("MainWindow", "正常量产"))

        self.comboBox_2.setItemText(0, _translate("MainWindow", "F00RJ01613"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "F00RJ04821"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "F00RJ00571"))
        # self.comboBox_2.currentIndexChanged.connect(self.selectionchange_2)
        self.目检型号 = self.comboBox_2.currentText()

        datetime = QDateTime.currentDateTime()
        self.text = datetime.toString('yyyy/MM/dd hh:mm:ss')

        self.label_1.setText(_translate("MainWindow", "目检台号"))

        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))

        self.pushButton_3.setText(_translate("MainWindow", "其 他"))

        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))

    def selectionchange_3(self,i):
        self.目检台号 = self.comboBox.currentText()
        self.目检型号 = self.comboBox_2.currentText()
        self.机床号 = self.comboBox_3.currentText()
        print(self.目检台号,self.目检型号,self.机床号)




    def showtime(self):
        datetime = QDateTime.currentDateTime()
        global text
        self.text = datetime.toString('yyyy/MM/dd hh:mm:ss' )
        self.label_6.setText(self.text)
        self.label_6.setFont(QFont("Roman times", 24, QFont.Bold))


    def Plot(self):  # 这里是绘图的关键
        self.plot_Figure = Figure_Canvas()  # 创建实例
        self.plot_FigureLayout = QGridLayout(self.groupBox)  # 利用栅格布局将图像与画板连接


    def drawHist(self):

        df = pd.read_excel(r'E:\test.xlsx')
        df2 = df['Postion'].value_counts().to_frame()
        self.reason = df2.index.to_list()
        self.reason.reverse()
        self.count_num = df2['Postion'].to_list()
        self.count_num.reverse()
        self.Plot()
        font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=8)
        self.count_num[1] = random.randint(100, 10000)
        print(self.count_num)
        self.plot_Figure.ax.barh(self.reason, self.count_num)  # 绘图
        self.plot_Figure.fig.canvas.draw_idle()
        self.plot_Figure.ax.set_yticklabels(self.reason, rotation=0, fontproperties=font_set)
        self.plot_Figure.fig.suptitle("Hist")
        self.plot_FigureLayout.addWidget(self.plot_Figure)

    def drawHist1(self):
        df = pd.read_excel(r'E:\test.xlsx').tail(100)
        df2 = df['Postion'].value_counts().to_frame()
        self.reason = df2.index.to_list()
        self.reason.reverse()
        self.count_num = df2['Postion'].to_list()
        self.count_num.reverse()
        self.count_num[1] = random.randint(100, 10000)
        self.Plot()
        font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=8)
        self.plot_Figure.ax.barh(self.reason, self.count_num)  # 绘图
        self.plot_Figure.ax.set_yticklabels(self.reason, rotation=0, fontproperties=font_set)
        self.plot_Figure.fig.suptitle("Hist")



    def ReSet(self):
        self.plot_Figure.deleteLater()  # 删除图像对象
        # self.plot_Figure.fig.clear()
        self.plot_FigureLayout.deleteLater()  # 删除布局
        self.drawHist()

        time.sleep(1)
        self.plot_Figure.deleteLater()  # 删除图像对象
        # self.plot_Figure.fig.clear()
        self.plot_FigureLayout.deleteLater()  # 删除布局
        self.drawHist()



class Figure_Canvas(FigureCanvas):
            def __init__(self, width=4, height=3, dpi=100):
                self.fig = Figure(figsize=(width, height), dpi=100)  # 设置长宽以及分辨率
                super(Figure_Canvas, self).__init__(self.fig)
                self.ax = self.fig.add_subplot(111)  # 创建axes对象实例，这个也可以在具体函数中添加


