# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a:\PythonProjects\AccountHolder\AccountHolder\SecurityQuestion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(170, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelQuestion = QtWidgets.QLabel(Dialog)
        self.labelQuestion.setGeometry(QtCore.QRect(136, 52, 311, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelQuestion.setFont(font)
        self.labelQuestion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuestion.setObjectName("labelQuestion")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 220, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonEnterAnswer = QtWidgets.QPushButton(Dialog)
        self.pushButtonEnterAnswer.setGeometry(QtCore.QRect(250, 272, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonEnterAnswer.setFont(font)
        self.pushButtonEnterAnswer.setObjectName("pushButtonEnterAnswer")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 330, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Account Recovery: Security Question"))
        self.labelTitle.setText(_translate("Dialog", "Security Question"))
        self.labelQuestion.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonEnterAnswer.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "Incorrect Answer"))
