# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LED_FND.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(288, 260)
        self.label_LED0 = QtWidgets.QLabel(window)
        self.label_LED0.setGeometry(QtCore.QRect(51, 131, 43, 73))
        self.label_LED0.setText("")
        self.label_LED0.setPixmap(QtGui.QPixmap("../samba_file/image_file/LED_ON.png"))
        self.label_LED0.setObjectName("label_LED0")
        self.label_LED1 = QtWidgets.QLabel(window)
        self.label_LED1.setGeometry(QtCore.QRect(190, 131, 43, 73))
        self.label_LED1.setText("")
        self.label_LED1.setPixmap(QtGui.QPixmap("../samba_file/image_file/LED_ON.png"))
        self.label_LED1.setObjectName("label_LED1")
        self.led0_btn = QtWidgets.QPushButton(window)
        self.led0_btn.setGeometry(QtCore.QRect(31, 210, 85, 30))
        self.led0_btn.setObjectName("led0_btn")
        self.led1_btn = QtWidgets.QPushButton(window)
        self.led1_btn.setGeometry(QtCore.QRect(170, 210, 85, 30))
        self.led1_btn.setObjectName("led1_btn")
        self.widget = QtWidgets.QWidget(window)
        self.widget.setGeometry(QtCore.QRect(31, 11, 229, 109))
        self.widget.setObjectName("widget")
        self.verticalLayout_FND = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_FND.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_FND.setObjectName("verticalLayout_FND")
        self.label_FND = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_FND.setFont(font)
        self.label_FND.setText("")
        self.label_FND.setPixmap(QtGui.QPixmap("../samba_file/image_file/FND.png"))
        self.label_FND.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FND.setObjectName("label_FND")
        self.verticalLayout_FND.addWidget(self.label_FND)
        self.label_help = QtWidgets.QLabel(self.widget)
        self.label_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_help.setObjectName("label_help")
        self.verticalLayout_FND.addWidget(self.label_help)
        self.lineEdit_FND = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_FND.setObjectName("lineEdit_FND")
        self.verticalLayout_FND.addWidget(self.lineEdit_FND)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "FND CNTL"))
        self.led0_btn.setText(_translate("window", "LED0"))
        self.led1_btn.setText(_translate("window", "LED2"))
        self.label_help.setText(_translate("window", "Input Datar(0~999999)"))

