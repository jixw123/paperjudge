# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(270, 100, 75, 31))
        self.select.setObjectName("select")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 260, 280, 230))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 260, 280, 230))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 471, 81))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_4.setObjectName("label_4")
        self.display_dir = QtWidgets.QLabel(self.centralwidget)
        self.display_dir.setGeometry(QtCore.QRect(120, 30, 301, 16))
        self.display_dir.setText("")
        self.display_dir.setObjectName("display_dir")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 54, 12))
        self.label_5.setObjectName("label_5")
        self.inputID = QtWidgets.QLineEdit(self.centralwidget)
        self.inputID.setGeometry(QtCore.QRect(70, 110, 161, 20))
        self.inputID.setInputMask("")
        self.inputID.setFrame(True)
        self.inputID.setObjectName("inputID")
        self.select_dir = QtWidgets.QPushButton(self.centralwidget)
        self.select_dir.setGeometry(QtCore.QRect(440, 30, 75, 23))
        self.select_dir.setObjectName("select_dir")
        self.correct = QtWidgets.QPushButton(self.centralwidget)
        self.correct.setGeometry(QtCore.QRect(440, 70, 75, 23))
        self.correct.setObjectName("correct")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menu = QtWidgets.QMenu(self.menufile)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menufile.addAction(self.menu.menuAction())
        self.menufile.addAction(self.action)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select.setText(_translate("MainWindow", "查询"))
        self.label_4.setText(_translate("MainWindow", "试卷文件夹目录"))
        self.label_5.setText(_translate("MainWindow", "输入学号"))
        self.inputID.setPlaceholderText(_translate("MainWindow", "输入要查询的学生学号"))
        self.select_dir.setText(_translate("MainWindow", "选择文件夹"))
        self.correct.setText(_translate("MainWindow", "开始阅卷"))
        self.menufile.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.menu_2.setTitle(_translate("MainWindow", "菜单"))
        self.action_2.setText(_translate("MainWindow", "试卷图片"))
        self.action_3.setText(_translate("MainWindow", "文件夹"))
        self.action_4.setText(_translate("MainWindow", "开始批卷"))
        self.action_5.setText(_translate("MainWindow", "查询结果"))
        self.action.setText(_translate("MainWindow", "退出"))
