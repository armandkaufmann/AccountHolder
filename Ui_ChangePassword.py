# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a:\PythonProjects\AccountHolder\AccountHolder\ChangePassword.ui'
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
        self.labelTitle.setGeometry(QtCore.QRect(180, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelDescription = QtWidgets.QLabel(Dialog)
        self.labelDescription.setGeometry(QtCore.QRect(90, 50, 421, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDescription.setFont(font)
        self.labelDescription.setObjectName("labelDescription")
        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setGeometry(QtCore.QRect(40, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.labelPasswordConfirm = QtWidgets.QLabel(Dialog)
        self.labelPasswordConfirm.setGeometry(QtCore.QRect(40, 200, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPasswordConfirm.setFont(font)
        self.labelPasswordConfirm.setObjectName("labelPasswordConfirm")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(200, 140, 311, 21))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPasswordConfirm = QtWidgets.QLineEdit(Dialog)
        self.lineEditPasswordConfirm.setGeometry(QtCore.QRect(200, 200, 311, 21))
        self.lineEditPasswordConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPasswordConfirm.setObjectName("lineEditPasswordConfirm")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 240, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonChangePassword = QtWidgets.QPushButton(Dialog)
        self.pushButtonChangePassword.setGeometry(QtCore.QRect(364, 310, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonChangePassword.setFont(font)
        self.pushButtonChangePassword.setObjectName("pushButtonChangePassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Change Password"))
        self.labelTitle.setText(_translate("Dialog", "Change Password"))
        self.labelDescription.setText(_translate("Dialog", "Ensure that new password is at minimum 8 characters long"))
        self.labelPassword.setText(_translate("Dialog", "Password:"))
        self.labelPasswordConfirm.setText(_translate("Dialog", "Confirm Password:"))
        self.label.setText(_translate("Dialog", "Password match/length"))
        self.pushButtonChangePassword.setText(_translate("Dialog", "Change Password"))
