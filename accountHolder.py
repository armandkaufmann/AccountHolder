import sys, random
from cryptography.fernet import Fernet
from PyQt5.QtCore import QFile, QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QLineEdit, QMainWindow, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
import accountFunctions
import Ui_AccountHolder
import Ui_CreateNewPlatform

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
    
    def accountsFromMemoryToFileSave(self) -> None:
        pass
    
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
    
    def listWidgetServiceAccounts_CurrentRowChanged(self) -> None:
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
        self.tabWidgeViewEditAccount.setEnabled(True)
        self.tabWidgeViewEditAccount.setCurrentIndex(0) #seting current index of tab to view account info tab
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password) #setting the echo mode of password line edit to password, in-case it was changed
        #View account info Tab
        self.lineEditUsername.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][0]) #setting username line edit
        self.lineEditPassword.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]) #setting password line edit
        self.lineEditEmail.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][2]) #setting email line edit 
        #edit account info Tab
        self.lineEditUsernameEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][0]) #setting username line edit
        self.lineEditPasswordEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]) #setting password line edit
        self.lineEditPasswordConfirmEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][1]) #setting confirm password line edit
        self.lineEditEmailEdit.setText(self.accounts[self.listWidgetServiceAccounts.currentRow()][1][self.listWidgetAccounts.currentRow()][2]) #setting email line edit 

    
    def pushButtonViewPassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
    
    def pushButtonHidePassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
    
    def pushButtonCopyPassword_Clicked(self) -> None:
        QApplication.clipboard().setText(self.lineEditPassword.text())
        QMessageBox.information(self, "Copied to clipboard", "Your password has been copied to your clipboard. Click the 'Ok' button on this window once you are done pasting your password for login, once you click the 'Ok' button your clipboard will automatically clear for security reasons", QMessageBox.Ok)
        QApplication.clipboard().setText(" ")
        
            
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
























if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountHolder()
    window.show()
    sys.exit(app.exec_())