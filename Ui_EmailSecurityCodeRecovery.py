# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a:\PythonProjects\AccountHolder\AccountHolder\EmailSecurityCodeRecovery.ui'
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
        self.labelTitle.setGeometry(QtCore.QRect(10, 10, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.labelSubtitle = QtWidgets.QLabel(Dialog)
        self.labelSubtitle.setGeometry(QtCore.QRect(10, 50, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSubtitle.setFont(font)
        self.labelSubtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSubtitle.setWordWrap(True)
        self.labelSubtitle.setObjectName("labelSubtitle")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 190, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 180, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.labelIncorrectCode = QtWidgets.QLabel(Dialog)
        self.labelIncorrectCode.setGeometry(QtCore.QRect(10, 260, 571, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelIncorrectCode.setFont(font)
        self.labelIncorrectCode.setStyleSheet("color:red;")
        self.labelIncorrectCode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIncorrectCode.setObjectName("labelIncorrectCode")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Account Recovery: Security Code"))
        self.labelTitle.setText(_translate("Dialog", "Security Code"))
        self.labelSubtitle.setText(_translate("Dialog", "Please check your email for the security code, if it is not there, please check your spam inbox. Email might take a couple of minutes to be recieved."))
        self.label.setText(_translate("Dialog", "Security Code:"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.labelIncorrectCode.setText(_translate("Dialog", "Incorrect Code"))
