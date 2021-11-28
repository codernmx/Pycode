import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import ui
import child
import other



if __name__ == '__main__':

    app = QApplication(sys.argv)
    # 实例化主窗口
    main = QMainWindow()
    main_ui = ui.Ui_MainWindow()
    main_ui.setupUi(main)
    main_ui.drawHist()
    # main_ui.ReSet()

    # 实例化子窗口
    child_page = QDialog()
    child_ui = child.Ui_Dialog()
    child_ui.setupUi(child_page)

    # 按钮绑定事件

    child_ui.pushButton.clicked.connect(main_ui.ReSet)
    # child_ui.pushButton.clicked.connect(main_ui.drawHist1)



    # 按钮绑定事件
    btn = main_ui.pushButton_2
    btn.clicked.connect(child_page.show)


    # 实例化子窗口
    other_page = QDialog()
    other_ui = other.Ui_Dialog()
    other_ui.setupUi(other_page)

    # 按钮绑定事件
    btn_3 = main_ui.pushButton_3
    btn_3.clicked.connect(other_page.show)


    main.show()


    sys.exit(app.exec_())


