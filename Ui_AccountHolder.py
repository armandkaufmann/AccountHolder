# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a:\PythonProjects\AccountHolder\AccountHolder\AccountHolder.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidgetAccountsEncryptDecrypt = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetAccountsEncryptDecrypt.setGeometry(QtCore.QRect(10, 10, 781, 741))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidgetAccountsEncryptDecrypt.setFont(font)
        self.tabWidgetAccountsEncryptDecrypt.setObjectName("tabWidgetAccountsEncryptDecrypt")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidgetServiceAccounts = QtWidgets.QListWidget(self.tab)
        self.listWidgetServiceAccounts.setGeometry(QtCore.QRect(395, 50, 361, 241))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listWidgetServiceAccounts.setFont(font)
        self.listWidgetServiceAccounts.setObjectName("listWidgetServiceAccounts")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(10, 320, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(396, 10, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frameAccountInfo = QtWidgets.QFrame(self.tab)
        self.frameAccountInfo.setGeometry(QtCore.QRect(0, 330, 771, 381))
        self.frameAccountInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAccountInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAccountInfo.setObjectName("frameAccountInfo")
        self.label_6 = QtWidgets.QLabel(self.frameAccountInfo)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 751, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.listWidgetAccounts = QtWidgets.QListWidget(self.frameAccountInfo)
        self.listWidgetAccounts.setGeometry(QtCore.QRect(10, 70, 256, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidgetAccounts.setFont(font)
        self.listWidgetAccounts.setObjectName("listWidgetAccounts")
        self.tabWidgeViewEditAccount = QtWidgets.QTabWidget(self.frameAccountInfo)
        self.tabWidgeViewEditAccount.setGeometry(QtCore.QRect(280, 50, 471, 321))
        self.tabWidgeViewEditAccount.setObjectName("tabWidgeViewEditAccount")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.labelUsername = QtWidgets.QLabel(self.tab_3)
        self.labelUsername.setGeometry(QtCore.QRect(50, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUsername.setFont(font)
        self.labelUsername.setObjectName("labelUsername")
        self.labelPassword = QtWidgets.QLabel(self.tab_3)
        self.labelPassword.setGeometry(QtCore.QRect(50, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditUsername = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditUsername.setGeometry(QtCore.QRect(140, 50, 241, 31))
        self.lineEditUsername.setText("")
        self.lineEditUsername.setReadOnly(True)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditPassword.setGeometry(QtCore.QRect(140, 100, 241, 31))
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setReadOnly(True)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonViewPassword = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonViewPassword.setGeometry(QtCore.QRect(50, 150, 101, 31))
        self.pushButtonViewPassword.setCheckable(False)
        self.pushButtonViewPassword.setObjectName("pushButtonViewPassword")
        self.pushButtonCopyPassword = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonCopyPassword.setGeometry(QtCore.QRect(280, 150, 101, 31))
        self.pushButtonCopyPassword.setObjectName("pushButtonCopyPassword")
        self.labelEmail = QtWidgets.QLabel(self.tab_3)
        self.labelEmail.setGeometry(QtCore.QRect(50, 240, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelEmail.setFont(font)
        self.labelEmail.setObjectName("labelEmail")
        self.lineEditEmail = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditEmail.setGeometry(QtCore.QRect(140, 230, 241, 31))
        self.lineEditEmail.setText("")
        self.lineEditEmail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditEmail.setReadOnly(True)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(20, 190, 421, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButtonHidePassword = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonHidePassword.setGeometry(QtCore.QRect(160, 150, 111, 31))
        self.pushButtonHidePassword.setCheckable(False)
        self.pushButtonHidePassword.setObjectName("pushButtonHidePassword")
        self.tabWidgeViewEditAccount.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButtonDeleteAccount = QtWidgets.QPushButton(self.tab_4)
        self.pushButtonDeleteAccount.setGeometry(QtCore.QRect(50, 250, 151, 31))
        self.pushButtonDeleteAccount.setObjectName("pushButtonDeleteAccount")
        self.lineEditEmailEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEditEmailEdit.setGeometry(QtCore.QRect(190, 200, 241, 31))
        self.lineEditEmailEdit.setText("")
        self.lineEditEmailEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditEmailEdit.setReadOnly(False)
        self.lineEditEmailEdit.setObjectName("lineEditEmailEdit")
        self.labelUsernameEdit = QtWidgets.QLabel(self.tab_4)
        self.labelUsernameEdit.setGeometry(QtCore.QRect(70, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUsernameEdit.setFont(font)
        self.labelUsernameEdit.setObjectName("labelUsernameEdit")
        self.lineEditUsernameEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEditUsernameEdit.setGeometry(QtCore.QRect(190, 10, 241, 31))
        self.lineEditUsernameEdit.setText("")
        self.lineEditUsernameEdit.setReadOnly(False)
        self.lineEditUsernameEdit.setObjectName("lineEditUsernameEdit")
        self.labelPasswordEdit = QtWidgets.QLabel(self.tab_4)
        self.labelPasswordEdit.setGeometry(QtCore.QRect(70, 70, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPasswordEdit.setFont(font)
        self.labelPasswordEdit.setObjectName("labelPasswordEdit")
        self.line_3 = QtWidgets.QFrame(self.tab_4)
        self.line_3.setGeometry(QtCore.QRect(20, 180, 421, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.labelEmail_2 = QtWidgets.QLabel(self.tab_4)
        self.labelEmail_2.setGeometry(QtCore.QRect(100, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelEmail_2.setFont(font)
        self.labelEmail_2.setObjectName("labelEmail_2")
        self.lineEditPasswordEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEditPasswordEdit.setGeometry(QtCore.QRect(190, 60, 241, 31))
        self.lineEditPasswordEdit.setText("")
        self.lineEditPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPasswordEdit.setReadOnly(False)
        self.lineEditPasswordEdit.setObjectName("lineEditPasswordEdit")
        self.pushButtonUpdateAccountInfo = QtWidgets.QPushButton(self.tab_4)
        self.pushButtonUpdateAccountInfo.setGeometry(QtCore.QRect(270, 250, 151, 31))
        self.pushButtonUpdateAccountInfo.setObjectName("pushButtonUpdateAccountInfo")
        self.labelPasswordConfirmEdit = QtWidgets.QLabel(self.tab_4)
        self.labelPasswordConfirmEdit.setGeometry(QtCore.QRect(10, 120, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPasswordConfirmEdit.setFont(font)
        self.labelPasswordConfirmEdit.setObjectName("labelPasswordConfirmEdit")
        self.lineEditPasswordConfirmEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEditPasswordConfirmEdit.setGeometry(QtCore.QRect(190, 110, 241, 31))
        self.lineEditPasswordConfirmEdit.setText("")
        self.lineEditPasswordConfirmEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPasswordConfirmEdit.setReadOnly(False)
        self.lineEditPasswordConfirmEdit.setObjectName("lineEditPasswordConfirmEdit")
        self.pushButtonViewPasswordEdit = QtWidgets.QPushButton(self.tab_4)
        self.pushButtonViewPasswordEdit.setGeometry(QtCore.QRect(210, 150, 101, 31))
        self.pushButtonViewPasswordEdit.setCheckable(False)
        self.pushButtonViewPasswordEdit.setObjectName("pushButtonViewPasswordEdit")
        self.pushButtonHidePasswordEdit = QtWidgets.QPushButton(self.tab_4)
        self.pushButtonHidePasswordEdit.setGeometry(QtCore.QRect(320, 150, 111, 31))
        self.pushButtonHidePasswordEdit.setCheckable(False)
        self.pushButtonHidePasswordEdit.setObjectName("pushButtonHidePasswordEdit")
        self.tabWidgeViewEditAccount.addTab(self.tab_4, "")
        self.label_7 = QtWidgets.QLabel(self.frameAccountInfo)
        self.label_7.setGeometry(QtCore.QRect(10, 290, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.pushButtonAddAccount = QtWidgets.QPushButton(self.frameAccountInfo)
        self.pushButtonAddAccount.setGeometry(QtCore.QRect(80, 330, 121, 31))
        self.pushButtonAddAccount.setObjectName("pushButtonAddAccount")
        self.labelPlatformName = QtWidgets.QLabel(self.frameAccountInfo)
        self.labelPlatformName.setGeometry(QtCore.QRect(6, 50, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelPlatformName.setFont(font)
        self.labelPlatformName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlatformName.setObjectName("labelPlatformName")
        self.groupBoxAddNewService = QtWidgets.QGroupBox(self.tab)
        self.groupBoxAddNewService.setGeometry(QtCore.QRect(20, 40, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxAddNewService.setFont(font)
        self.groupBoxAddNewService.setStyleSheet("")
        self.groupBoxAddNewService.setObjectName("groupBoxAddNewService")
        self.label_2 = QtWidgets.QLabel(self.groupBoxAddNewService)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButtonAddNewAccountService = QtWidgets.QPushButton(self.groupBoxAddNewService)
        self.pushButtonAddNewAccountService.setGeometry(QtCore.QRect(130, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAddNewAccountService.setFont(font)
        self.pushButtonAddNewAccountService.setObjectName("pushButtonAddNewAccountService")
        self.groupBoxDeleteAccountService = QtWidgets.QGroupBox(self.tab)
        self.groupBoxDeleteAccountService.setGeometry(QtCore.QRect(20, 190, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDeleteAccountService.setFont(font)
        self.groupBoxDeleteAccountService.setStyleSheet("")
        self.groupBoxDeleteAccountService.setObjectName("groupBoxDeleteAccountService")
        self.label_4 = QtWidgets.QLabel(self.groupBoxDeleteAccountService)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.pushButtonDeleteAccountService = QtWidgets.QPushButton(self.groupBoxDeleteAccountService)
        self.pushButtonDeleteAccountService.setGeometry(QtCore.QRect(140, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonDeleteAccountService.setFont(font)
        self.pushButtonDeleteAccountService.setObjectName("pushButtonDeleteAccountService")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(396, 289, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.tabWidgetAccountsEncryptDecrypt.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidgetFiles = QtWidgets.QListWidget(self.tab_2)
        self.listWidgetFiles.setGeometry(QtCore.QRect(20, 80, 731, 192))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.listWidgetFiles.setFont(font)
        self.listWidgetFiles.setAutoFillBackground(False)
        self.listWidgetFiles.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidgetFiles.setObjectName("listWidgetFiles")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 9, 731, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBoxEncryption = QtWidgets.QGroupBox(self.tab_2)
        self.groupBoxEncryption.setGeometry(QtCore.QRect(210, 380, 351, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxEncryption.setFont(font)
        self.groupBoxEncryption.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxEncryption.setObjectName("groupBoxEncryption")
        self.pushButtonAddFile_2 = QtWidgets.QPushButton(self.groupBoxEncryption)
        self.pushButtonAddFile_2.setGeometry(QtCore.QRect(40, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAddFile_2.setFont(font)
        self.pushButtonAddFile_2.setObjectName("pushButtonAddFile_2")
        self.pushButtonAddFile_3 = QtWidgets.QPushButton(self.groupBoxEncryption)
        self.pushButtonAddFile_3.setGeometry(QtCore.QRect(180, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAddFile_3.setFont(font)
        self.pushButtonAddFile_3.setObjectName("pushButtonAddFile_3")
        self.pushButtonAddFile = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonAddFile.setGeometry(QtCore.QRect(250, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAddFile.setFont(font)
        self.pushButtonAddFile.setWhatsThis("")
        self.pushButtonAddFile.setObjectName("pushButtonAddFile")
        self.pushButtonRemoveFile = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonRemoveFile.setGeometry(QtCore.QRect(400, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonRemoveFile.setFont(font)
        self.pushButtonRemoveFile.setObjectName("pushButtonRemoveFile")
        self.line_4 = QtWidgets.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(20, 330, 731, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 731, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.groupBoxEncryption_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBoxEncryption_2.setGeometry(QtCore.QRect(210, 530, 351, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxEncryption_2.setFont(font)
        self.groupBoxEncryption_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxEncryption_2.setObjectName("groupBoxEncryption_2")
        self.pushButtonAddFile_6 = QtWidgets.QPushButton(self.groupBoxEncryption_2)
        self.pushButtonAddFile_6.setGeometry(QtCore.QRect(40, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAddFile_6.setFont(font)
        self.pushButtonAddFile_6.setObjectName("pushButtonAddFile_6")
        self.pushButtonAddFile_7 = QtWidgets.QPushButton(self.groupBoxEncryption_2)
        self.pushButtonAddFile_7.setGeometry(QtCore.QRect(180, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAddFile_7.setFont(font)
        self.pushButtonAddFile_7.setObjectName("pushButtonAddFile_7")
        self.tabWidgetAccountsEncryptDecrypt.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuAccount.addAction(self.actionSettings)
        self.menubar.addAction(self.menuAccount.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidgetAccountsEncryptDecrypt.setCurrentIndex(0)
        self.tabWidgeViewEditAccount.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Account Holder"))
        self.listWidgetServiceAccounts.setStatusTip(_translate("MainWindow", "List of all platforms stored on the program."))
        self.label.setText(_translate("MainWindow", "Platform"))
        self.label_6.setText(_translate("MainWindow", "Account Information"))
        self.listWidgetAccounts.setStatusTip(_translate("MainWindow", "List of all accounts stored within selected platform."))
        self.tabWidgeViewEditAccount.setStatusTip(_translate("MainWindow", "View and edit the information about the a specific account in the platform selected."))
        self.labelUsername.setText(_translate("MainWindow", "Username:"))
        self.labelPassword.setText(_translate("MainWindow", "Password:"))
        self.pushButtonViewPassword.setStatusTip(_translate("MainWindow", "View the password of the account."))
        self.pushButtonViewPassword.setText(_translate("MainWindow", "View password"))
        self.pushButtonCopyPassword.setStatusTip(_translate("MainWindow", "Copy the password to the clipboard, password will automatically clear from the clipboard after pressing \"Ok\" on the prompt."))
        self.pushButtonCopyPassword.setText(_translate("MainWindow", "Copy password"))
        self.labelEmail.setText(_translate("MainWindow", "Email:"))
        self.pushButtonHidePassword.setStatusTip(_translate("MainWindow", "Hide the password and convert to a secure string."))
        self.pushButtonHidePassword.setText(_translate("MainWindow", "Hide Password"))
        self.tabWidgeViewEditAccount.setTabText(self.tabWidgeViewEditAccount.indexOf(self.tab_3), _translate("MainWindow", "View Account Info"))
        self.pushButtonDeleteAccount.setStatusTip(_translate("MainWindow", "Delete the selected account from the stored platform."))
        self.pushButtonDeleteAccount.setText(_translate("MainWindow", "Delete Account"))
        self.labelUsernameEdit.setText(_translate("MainWindow", "Username:"))
        self.labelPasswordEdit.setText(_translate("MainWindow", "Password:"))
        self.labelEmail_2.setText(_translate("MainWindow", "Email:"))
        self.pushButtonUpdateAccountInfo.setStatusTip(_translate("MainWindow", "If changes are made, click this to update the information."))
        self.pushButtonUpdateAccountInfo.setText(_translate("MainWindow", "Update Account"))
        self.labelPasswordConfirmEdit.setText(_translate("MainWindow", "Confirm Password:"))
        self.pushButtonViewPasswordEdit.setText(_translate("MainWindow", "View password"))
        self.pushButtonHidePasswordEdit.setText(_translate("MainWindow", "Hide Password"))
        self.tabWidgeViewEditAccount.setTabText(self.tabWidgeViewEditAccount.indexOf(self.tab_4), _translate("MainWindow", "Edit Account Info"))
        self.label_7.setText(_translate("MainWindow", "Click on a specific account for the selected platform to view or edit account details"))
        self.pushButtonAddAccount.setStatusTip(_translate("MainWindow", "Add additional accounts to the same platform."))
        self.pushButtonAddAccount.setText(_translate("MainWindow", "Add New Account"))
        self.labelPlatformName.setText(_translate("MainWindow", "platformName"))
        self.groupBoxAddNewService.setTitle(_translate("MainWindow", "New platform"))
        self.label_2.setText(_translate("MainWindow", "Add a new platform and accompanying account for a platform not stored in the program"))
        self.pushButtonAddNewAccountService.setStatusTip(_translate("MainWindow", "Create a new platform that holds the account specific to that platform."))
        self.pushButtonAddNewAccountService.setText(_translate("MainWindow", "Add New"))
        self.groupBoxDeleteAccountService.setTitle(_translate("MainWindow", "Delete a platform and all accounts within"))
        self.label_4.setText(_translate("MainWindow", "Select a specific platform (in the list to the right) and click delete"))
        self.pushButtonDeleteAccountService.setStatusTip(_translate("MainWindow", "Deleting a platform will remove the platform and all accompanying accounts in the program."))
        self.pushButtonDeleteAccountService.setText(_translate("MainWindow", "Delete"))
        self.label_5.setText(_translate("MainWindow", "Click on an account to view password, view account platform information and add additional accounts to a specific platform"))
        self.tabWidgetAccountsEncryptDecrypt.setTabText(self.tabWidgetAccountsEncryptDecrypt.indexOf(self.tab), _translate("MainWindow", "Accounts"))
        self.label_3.setText(_translate("MainWindow", "Files"))
        self.groupBoxEncryption.setTitle(_translate("MainWindow", "Encryption"))
        self.pushButtonAddFile_2.setStatusTip(_translate("MainWindow", "Encrypt a selected file."))
        self.pushButtonAddFile_2.setText(_translate("MainWindow", "Encrypt File"))
        self.pushButtonAddFile_3.setStatusTip(_translate("MainWindow", "Encrypt all files in the list."))
        self.pushButtonAddFile_3.setText(_translate("MainWindow", "Encrypt All Files"))
        self.pushButtonAddFile.setStatusTip(_translate("MainWindow", "Add a file to the list to encrypt and decrypt."))
        self.pushButtonAddFile.setText(_translate("MainWindow", "Load File"))
        self.pushButtonRemoveFile.setStatusTip(_translate("MainWindow", "Remove a file from the list. This does not remove the file from your computer."))
        self.pushButtonRemoveFile.setText(_translate("MainWindow", "Remove File"))
        self.label_8.setText(_translate("MainWindow", "Encrypt files to protect sensitive information. Decrypt file before opening/using."))
        self.groupBoxEncryption_2.setTitle(_translate("MainWindow", "Decryption"))
        self.pushButtonAddFile_6.setStatusTip(_translate("MainWindow", "Decrypt selected encrypted file."))
        self.pushButtonAddFile_6.setText(_translate("MainWindow", "Decrypt File"))
        self.pushButtonAddFile_7.setStatusTip(_translate("MainWindow", "Decrypt all encrypted files in the list."))
        self.pushButtonAddFile_7.setText(_translate("MainWindow", "Decrypt All Files"))
        self.tabWidgetAccountsEncryptDecrypt.setTabText(self.tabWidgetAccountsEncryptDecrypt.indexOf(self.tab_2), _translate("MainWindow", "Encrypt/Decrypt Files"))
        self.menuAccount.setTitle(_translate("MainWindow", "Settings"))
        self.actionSettings.setText(_translate("MainWindow", "Account Settings"))
