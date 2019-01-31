# Copyright (C) 2019 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_MainWin(object):
    def setupUi(self, Form_MainWin):
        Form_MainWin.setObjectName("Form_MainWin")
        Form_MainWin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Form_MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_browseFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browseFolder.setGeometry(QtCore.QRect(70, 20, 201, 28))
        self.pushButton_browseFolder.setObjectName("pushButton_browseFolder")
        self.label_folderSelected = QtWidgets.QLabel(self.centralwidget)
        self.label_folderSelected.setGeometry(QtCore.QRect(180, 60, 381, 16))
        self.label_folderSelected.setObjectName("label_folderSelected")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 91, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit_outputGen = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_outputGen.setGeometry(QtCore.QRect(60, 170, 651, 341))
        self.textEdit_outputGen.setObjectName("textEdit_outputGen")
        self.pushButton_genSigs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_genSigs.setGeometry(QtCore.QRect(70, 140, 171, 28))
        self.pushButton_genSigs.setObjectName("pushButton_genSigs")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 100, 101, 16))
        self.label.setObjectName("label")
        self.lineEdit_sdkApiDefine = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sdkApiDefine.setGeometry(QtCore.QRect(190, 100, 471, 22))
        self.lineEdit_sdkApiDefine.setObjectName("lineEdit_sdkApiDefine")
        Form_MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form_MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Form_MainWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form_MainWin)
        self.statusbar.setObjectName("statusbar")
        Form_MainWin.setStatusBar(self.statusbar)

        self.retranslateUi(Form_MainWin)
        self.pushButton_browseFolder.clicked.connect(Form_MainWin.browse_folder)
        self.pushButton_genSigs.clicked.connect(Form_MainWin.generate_sigs)
        QtCore.QMetaObject.connectSlotsByName(Form_MainWin)

    def retranslateUi(self, Form_MainWin):
        _translate = QtCore.QCoreApplication.translate
        Form_MainWin.setWindowTitle(_translate("Form_MainWin", "MainWindow"))
        self.pushButton_browseFolder.setText(_translate("Form_MainWin", "Browse folder of header files"))
        self.label_folderSelected.setText(_translate("Form_MainWin", "TextLabel"))
        self.label_2.setText(_translate("Form_MainWin", "Folder selected"))
        self.pushButton_genSigs.setText(_translate("Form_MainWin", "Generate CFFI signatures"))
        self.label.setText(_translate("Form_MainWin", "SDK_API_define"))

