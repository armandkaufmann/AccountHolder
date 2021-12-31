import sys, random
from cryptography.fernet import Fernet
from PyQt5.QtCore import QFile, QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QLineEdit, QMainWindow, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
import accountFunctions
import Ui_AccountHolder
import Ui_CreateNewPlatform
import Ui_AddNewAccountToPlatform

class AccountHolder(QMainWindow, Ui_AccountHolder.Ui_MainWindow):
    """Main account holder program"""
    def __init__(self, parent=None):
        super(AccountHolder, self).__init__(parent)
        self.setupUi(self)
        self.frameAccountInfo.hide()
        self.pushButtonDeleteAccountService.setEnabled(False)
        #account info
        self.f = None
        self.key = None
        self.accountInfo = None
        self.accounts = [] #structure [ [platform1, [ [account1_username, account1_password, account1_email],  [account1_username, account1_password, account1_email]] ]]
        self.getKey() #get key and f from file
        self.getAccountInfo() #get account username and password
        self.getAccountsToMemory() #initially load accounts file into memory, automatically adds to list widget
        #signals
        self.pushButtonAddNewAccountService.clicked.connect(self.pushButtonAddNewAccountService_Clicked)
        self.listWidgetServiceAccounts.currentRowChanged.connect(self.listWidgetServiceAccounts_CurrentRowChanged)
        self.listWidgetAccounts.currentRowChanged.connect(self.listWidgetAccounts_CurrentRowChanged)
        self.pushButtonViewPassword.clicked.connect(self.pushButtonViewPassword_Clicked)
        self.pushButtonHidePassword.clicked.connect(self.pushButtonHidePassword_Clicked)
        self.pushButtonCopyPassword.clicked.connect(self.pushButtonCopyPassword_Clicked)
        self.pushButtonDeleteAccountService.clicked.connect(self.pushButtonDeleteAccountService_Clicked)
        self.pushButtonViewPasswordEdit.clicked.connect(self.pushButtonViewPasswordEdit_Clicked)
        self.pushButtonHidePasswordEdit.clicked.connect(self.pushButtonHidePasswordEdit_Clicked)
        self.pushButtonAddAccount.clicked.connect(self.pushButtonAddAccount_Clicked)
        self.pushButtonDeleteAccount.clicked.connect(self.pushButtonDeleteAccount_Clicked)
        self.pushButtonUpdateAccountInfo.clicked.connect(self.pushButtonUpdateAccountInfo_Clicked)

    def getKey(self) -> None:
        """Gets the encryption key"""
        try:
            self.key = accountFunctions.loadKey()
        except FileNotFoundError:
            QMessageBox.information(self, "Error", "Could not find encryption key file.", QMessageBox.Ok)
        else:
            self.f = Fernet(self.key)
    
    def getAccountInfo(self) -> None:
        """Gets the account info"""
        try:
            self.accountInfo = accountFunctions.loadUserAccountInfo(self.f)
        except FileNotFoundError:
            QMessageBox.information(self, "Error", "Could not find the account file.", QMessageBox.Ok)
    
    def getAccountsToMemory(self) -> None:
        """To initially load the accounts from file to memory. If there are no accounts, or no account """
        if accountFunctions.checkAccountFileExist():
            self.accounts = accountFunctions.loadUserAccounts(self.f)
            for item in self.accounts:
                self.listWidgetServiceAccounts.addItem(item[0])
        else:
            QMessageBox.information(self, "No stored accounts", "You do not have any accounts stored in the program yet. Please add accounts to the program.", QMessageBox.Ok)
    
    def accountsFromMemoryToListWidget(self) -> None:
        self.listWidgetServiceAccounts.clear() #clearing the list widget from items
        for item in self.accounts:
            self.listWidgetServiceAccounts.addItem(item[0])
    
    def pushButtonAddNewAccountService_Clicked(self) -> None:
        popAccount = CreateNewPlatform(self)
        popAccount.show()
        popAccount.exec_()
        if popAccount.account == None:
            pass
        elif popAccount.account != None:
            self.accounts.append(popAccount.account) #adding the account to accounts in memory
            self.accountsFromMemoryToListWidget() #updating the list widget
            accountFunctions.saveUserAccounts(self.accounts, self.f) #saving to file, by overwritting current file
            if len(self.accounts) == 1:
                self.listWidgetServiceAccounts.setCurrentRow(0)
            else:
                self.listWidgetServiceAccounts.setCurrentRow(len(self.accounts) - 1)
    
    def reloadListWidgetServiceAccounts(self) -> None:
        """Reload the accounts in the list widget"""
        self.listWidgetServiceAccounts.clear()
        for item in self.accounts:
            self.listWidgetServiceAccounts.addItem(item[0])
    
    def reloadListWidgetAccounts(self) -> None:
        self.listWidgetAccounts.clear()
        for account in self.accounts[self.listWidgetServiceAccounts.currentRow()][1]:
            self.listWidgetAccounts.addItem(account[0])
    
    def listWidgetServiceAccounts_CurrentRowChanged(self) -> None:
        if len(self.accounts) > 0:
            self.tabWidgeViewEditAccount.setCurrentIndex(0)
            self.pushButtonDeleteAccountService.setEnabled(True)
            self.listWidgetAccounts.clear()
            for item in self.accounts[self.listWidgetServiceAccounts.currentRow()][1]:
                self.listWidgetAccounts.addItem(item[0])
            self.labelPlatformName.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][0]) #platform title ontop of the list widget
            self.tabWidgeViewEditAccount.setEnabled(False)
            #Resetting the line edit to empty string
            self.lineEditUsername.setText("")
            self.lineEditPassword.setText("")
            self.lineEditEmail.setText("")
            #showing the account info frame that has the view account info tab, and edit account info tab
            self.frameAccountInfo.show()
    
    def listWidgetAccounts_CurrentRowChanged(self) -> None:
        if len(self.accounts[self.listWidgetServiceAccounts.currentRow()][1]) > 0:
            self.tabWidgeViewEditAccount.setEnabled(True)
            self.tabWidgeViewEditAccount.setCurrentIndex(0) #seting current index of tab to view account info tab
            self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password) #setting the echo mode of password line edit to password, in-case it was changed
            #View account info Tab
            self.lineEditUsername.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][0]) #setting username line edit
            self.lineEditPassword.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]) #setting password line edit
            self.lineEditEmail.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][2]) #setting email line edit 
            #edit account info Tab
            self.lineEditPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password) #setting echo mode to password
            self.lineEditPasswordConfirmEdit.setEchoMode(QLineEdit.EchoMode.Password) #setting echo mode to password
            self.lineEditUsernameEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][0]) #setting username line edit
            self.lineEditPasswordEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]) #setting password line edit
            self.lineEditPasswordConfirmEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]) #setting confirm password line edit
            self.lineEditEmailEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][2]) #setting email line edit 

    
    def pushButtonViewPassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
    
    def pushButtonHidePassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
    
    def pushButtonViewPasswordEdit_Clicked(self) -> None:
        self.lineEditPasswordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEditPasswordConfirmEdit.setEchoMode(QLineEdit.EchoMode.Normal)
    
    def pushButtonHidePasswordEdit_Clicked(self) -> None:
        self.lineEditPasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditPasswordConfirmEdit.setEchoMode(QLineEdit.EchoMode.Password)
    
    def pushButtonCopyPassword_Clicked(self) -> None:
        """Copy password of selected account in the platform to clipboard"""
        QApplication.clipboard().setText(self.lineEditPassword.text())
        QMessageBox.information(self, "Copied to clipboard", "Your password has been copied to your clipboard. Click the 'Ok' button on this window once you are done pasting your password for login, once you click the 'Ok' button your clipboard will automatically clear for security reasons", QMessageBox.Ok)
        QApplication.clipboard().setText(" ")
    
    def pushButtonDeleteAccountService_Clicked(self) -> None:
        """Delete a platform in the platform list widget"""
        deletePlatform = QMessageBox.question(self, 'Delete Platform', f'Are you sure you want to delete the {self.accounts[self.listWidgetServiceAccounts.currentRow()][0]} platform and all associated accounts?', QMessageBox.Yes, QMessageBox.No)
        if deletePlatform == QMessageBox.Yes:
            self.accounts.pop(self.listWidgetServiceAccounts.currentRow())
            self.reloadListWidgetServiceAccounts() #resetting the list widget
            accountFunctions.saveUserAccounts(self.accounts, self.f)
            self.frameAccountInfo.hide()
            if len(self.accounts) == 0:
                self.pushButtonDeleteAccountService.setEnabled(False)
    
    def pushButtonAddAccount_Clicked(self) -> None:
        """Adding new account to selected platform"""
        popAccount = CreateNewAccountInPlatform(self, self.accounts[self.listWidgetServiceAccounts.currentRow()][0])
        popAccount.show()
        popAccount.exec_()
        if popAccount.account == None:
            pass
        elif popAccount.account != None:
            self.accounts[self.listWidgetServiceAccounts.currentRow()][1].append(popAccount.account)
            self.reloadListWidgetAccounts()
            accountFunctions.saveUserAccounts(self.accounts, self.f)
            if len(self.accounts[self.listWidgetServiceAccounts.currentRow()][1]) == 1:
                self.listWidgetAccounts.setCurrentRow(0)
            else:
                self.listWidgetAccounts.setCurrentRow(len(self.accounts[self.listWidgetServiceAccounts.currentRow()][1]) - 1)
    
    def pushButtonDeleteAccount_Clicked(self) -> None:
        """Delete account within a platform"""
        deleteAccount = QMessageBox.question(self, "Delete Account", f"Are you sure you want to delete your {self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][0]} account?", QMessageBox.Yes, QMessageBox.No)
        if deleteAccount == QMessageBox.Yes:
            self.accounts[self.listWidgetServiceAccounts.currentRow()][1].pop(self.listWidgetAccounts.currentRow())
            self.reloadListWidgetAccounts()
            accountFunctions.saveUserAccounts(self.accounts, self.f)
            self.tabWidgeViewEditAccount.setCurrentIndex(0)
            self.tabWidgeViewEditAccount.setEnabled(False)
            self.lineEditUsername.setText("")
            self.lineEditPassword.setText("")
            self.lineEditEmail.setText("")
    
    def pushButtonUpdateAccountInfo_Clicked(self) -> None:
        changesMade = False
        if self.lineEditUsernameEdit.text() != self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][0]:
            changesMade = True
        if self.lineEditPasswordEdit.text() != self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]:
            changesMade = True
        if self.lineEditPasswordConfirmEdit.text() != self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]:
            changesMade = True
        if self.lineEditEmailEdit.text() != self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][2]:
            changesMade = True
        if changesMade:
            updateAccount = QMessageBox.question(self, "Update account?", "Are you sure you want to update the details of this account?", QMessageBox.Yes, QMessageBox.No)
            if updateAccount == QMessageBox.Yes:
                if self.lineEditPasswordEdit.text() == self.lineEditPasswordConfirmEdit.text(): #if the passwords match
                    self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()] = [self.lineEditUsernameEdit.text(), self.lineEditPasswordEdit.text(), self.lineEditEmailEdit.text()]
                    listWidgetAccIdx = self.listWidgetAccounts.currentRow()
                    self.reloadListWidgetAccounts()
                    accountFunctions.saveUserAccounts(self.accounts, self.f)
                    self.listWidgetAccounts.setCurrentRow(listWidgetAccIdx)
                    self.tabWidgeViewEditAccount.setCurrentIndex(1)
                    QMessageBox.information(self, "Account Update Successful", "Account has been successfully updated.", QMessageBox.Ok)
                else: #passwords don't match
                    QMessageBox.information(self, "Password does not match", "The new password you have entered does not match, please ensure that the passwords match.", QMessageBox.Ok)
                    self.lineEditPasswordEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1])
                    self.lineEditPasswordConfirmEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1])


            
class CreateNewPlatform(QDialog, Ui_CreateNewPlatform.Ui_Dialog):
    """Security question dialog window for account recovery"""

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.labelPlatformExample_2.hide()
        self.account = None
        #signlas
        self.pushButtonCreateAccount.clicked.connect(self.pushButtonCreateAccount_Clicked)
        self.checkBoxEmailUsername.stateChanged.connect(self.checkBoxEmailUsername_StateChanged)
        self.pushButtonViewPassword.clicked.connect(self.pushButtonViewPassword_Clicked)
        self.pushButtonHidePassword.clicked.connect(self.pushButtonHidePassword_Clicked)

    def pushButtonViewPassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.EchoMode.Normal)

    def pushButtonHidePassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.EchoMode.Password)
    
    def pushButtonCreateAccount_Clicked(self) -> None:
        if self.checkAllFields():
            QMessageBox.information(self, "Missing Account Information", "Please fill out the missing account information to create account", QMessageBox.Ok)
        else: #structure [ [platform1, [account1_username, account1_password, account1_email]], [platform2, [account1_username, account1_password, account1_email]] ]
            if self.checkPasswordMatch():
                self.labelPlatformExample_2.hide()
                if self.checkBoxEmailUsername.isChecked():
                    self.account = [self.lineEditPlatform.text().title(), [[self.lineEditUsername_2.text(), self.lineEditPassword.text(), self.lineEditUsername_2.text()]]]
                else:
                    self.account = [self.lineEditPlatform.text().title(), [[self.lineEditUsername.text(), self.lineEditPassword.text(), self.lineEditUsername_2.text()]]]
                QMessageBox.information(self, "Successfully created account", "Your account has been succesfully created, account will be added to the program.", QMessageBox.Ok)
                self.close()
            else:
                self.labelPlatformExample_2.show()
    
    def checkPasswordMatch(self) -> bool:
        if self.lineEditPassword.text() == self.lineEditPasswordConfirm.text():
            return True
        else:
            return False 
    
    def checkAllFields(self) -> bool:
        missingInfo = 0
        if self.lineEditPlatform.text() == "":
            missingInfo = 1
        if self.lineEditUsername_2.text() == "":
            missingInfo = 1
        if self.lineEditUsername.text() == "" and self.checkBoxEmailUsername.isChecked() == False:
            missingInfo = 1
        if self.lineEditPassword.text() == "":
            missingInfo = 1
        if self.lineEditPasswordConfirm.text() == "":
            missingInfo = 1
        return missingInfo
    
    def checkBoxEmailUsername_StateChanged(self):
        if self.checkBoxEmailUsername.isChecked():
            self.lineEditUsername.setEnabled(False)
        else:
            self.lineEditUsername.setEnabled(True)

class CreateNewAccountInPlatform(QDialog, Ui_AddNewAccountToPlatform.Ui_Dialog):
    """Create New account in a platform"""

    def __init__(self, parent, platformName : str):
        super().__init__(parent)
        self.setupUi(self)
        self.platformName = platformName
        self.labelPlatformExample_2.hide()
        self.labelTitle.setText(f"Add new {self.platformName} account")
        self.account = None
        #signlas
        self.pushButtonCreateAccount.clicked.connect(self.pushButtonCreateAccount_Clicked)
        self.checkBoxEmailUsername.stateChanged.connect(self.checkBoxEmailUsername_StateChanged)
        self.pushButtonViewPassword.clicked.connect(self.pushButtonViewPassword_Clicked)
        self.pushButtonHidePassword.clicked.connect(self.pushButtonHidePassword_Clicked)
    
    def pushButtonViewPassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.EchoMode.Normal)

    def pushButtonHidePassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.EchoMode.Password)
    
    def pushButtonCreateAccount_Clicked(self) -> None:
        if self.checkAllFields():
            QMessageBox.information(self, "Missing Account Information", "Please fill out the missing account information to create account", QMessageBox.Ok)
        else: #structure [account1_username, account1_password, account1_email]
            if self.checkPasswordMatch(): #if passwords match
                self.labelPlatformExample_2.hide()
                if self.checkBoxEmailUsername.isChecked():
                    self.account = [self.lineEditUsername_2.text(), self.lineEditPassword.text(), self.lineEditUsername_2.text()]
                else:
                    self.account = [self.lineEditUsername.text(), self.lineEditPassword.text(), self.lineEditUsername_2.text()]
                QMessageBox.information(self, "Successfully created account", f"Your account has been succesfully created, account will be added to your {self.platformName} account", QMessageBox.Ok)
                self.close()
            else:
                self.labelPlatformExample_2.show()
    
    def checkPasswordMatch(self) -> bool:
        if self.lineEditPassword.text() == self.lineEditPasswordConfirm.text():
            return True
        else:
            return False 
    
    def checkAllFields(self) -> bool:
        missingInfo = 0
        if self.lineEditUsername_2.text() == "":
            missingInfo = 1
        if self.lineEditUsername.text() == "" and self.checkBoxEmailUsername.isChecked() == False:
            missingInfo = 1
        if self.lineEditPassword.text() == "":
            missingInfo = 1
        if self.lineEditPasswordConfirm.text() == "":
            missingInfo = 1
        return missingInfo
    
    def checkBoxEmailUsername_StateChanged(self):
        if self.checkBoxEmailUsername.isChecked():
            self.lineEditUsername.setEnabled(False)
        else:
            self.lineEditUsername.setEnabled(True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountHolder()
    window.show()
    sys.exit(app.exec_())