import sys, random
from cryptography.fernet import Fernet
from PyQt5.QtCore import QFile, QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QLineEdit, QMainWindow, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
import accountFunctions
import Ui_AccountHolder
import Ui_CreateNewPlatform
import Ui_AddNewAccountToPlatform
import Ui_AccountSettingsWindow

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
        self.filesToEncrypt = []
        self.getKey() #get key and f from file
        self.getAccountInfo() #get account username and password
        self.getAccountsToMemory() #initially load accounts file into memory, automatically adds to list widget
        self.loadFilesToEncrypt() #structure -> [[filePath, isEncrypted (True or False)]]
        self.disableFileOption()
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
        #settings
        self.actionSettings.triggered.connect(self.actionSettings_Triggered)
        #load files and ecnrypt/decrypt
        self.pushButtonAddFile.clicked.connect(self.pushButtonAddFile_Clicked)
        self.listWidgetFiles.currentRowChanged.connect(self.listWidgetFiles_CurrentRowChanged)
        self.pushButtonRemoveFile.clicked.connect(self.pushButtonRemoveFile_Clicked)
        self.pushButtonAddFile_2.clicked.connect(self.pushButtonAddFile_2_Clicked) #encrypt file button
        self.pushButtonAddFile_6.clicked.connect(self.pushButtonAddFile_6_Clicked) #decrypt file button
        self.pushButtonAddFile_3.clicked.connect(self.pushButtonAddFile_3_Clicked) #encrypt all files button
        self.pushButtonAddFile_7.clicked.connect(self.pushButtonAddFile_7_Clicked) #decrypt all files button
    
    def actionSettings_Triggered(self) -> None:
        """Account settings window, if changes are made then changes will be saved to user account info file"""
        accountSettings = AccountSettingsWindow(self, self.accountInfo)
        accountSettings.show()
        accountSettings.exec_()
        if accountSettings.changesMade: #if there are changes made to the account information/security question
            self.accountInfo = accountSettings.accountInfo
            accountFunctions.saveUserAccountInfo(self.accountInfo, self.f)

    def getKey(self) -> None:
        """Gets the encryption key"""
        try:
            self.key = accountFunctions.loadKey()
        except FileNotFoundError: #can't find the encryption key
            QMessageBox.information(self, "Error", "Could not find encryption key file.", QMessageBox.Ok)
            self.close()
        else:
            self.f = Fernet(self.key)
    
    def getAccountInfo(self) -> None:
        """Gets the account info"""
        try:
            self.accountInfo = accountFunctions.loadUserAccountInfo(self.f)
        except FileNotFoundError: #can't find the account info
            QMessageBox.information(self, "Error", "Could not find the account file.", QMessageBox.Ok)
            self.close()
    
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
        """Update account info button is pushed. If there are changes made, then changes will be saved to accounts file"""
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
    
    def loadFilesToEncrypt(self) -> None:
        """Loads the files to encrypt to memory, and update the list widget. If the file"""
        if accountFunctions.checkFileToEncryptExist("ox04.pkl"):
            filesToEncrypt = accountFunctions.loadFilesToEncryptList(self.f) #structure -> [[filepath, isEncrypted(True or False)]]
            if filesToEncrypt != []:
                self.filesToEncrypt = filesToEncrypt
                self.updateFilesListWidget()
                self.pushButtonAddFile_3.setEnabled(True)
                self.enableFileOptions()
                self.disableFileOption()
        else:
            self.filesToEncrypt = [] #return empty list

    def getFileName(self) -> str:
        """File dialog will open, user will point to the file, returns the full path of the file"""
        return QFileDialog.getOpenFileName(self, "Load File", "C:\\")[0] #open a file dialog box to point to file
    
    def updateFilesListWidget(self) -> None:
        """Updates the files list widget"""
        self.listWidgetFiles.clear() #clear the list widget
        if self.filesToEncrypt != []: #if the files to encrypt is not empty
            for fileE in self.filesToEncrypt: #adding all the files to the list widget
                fileName = fileE[0].split("/")[-1]
                self.listWidgetFiles.addItem(f"{fileName}\t\t[{'ENCRYPTED' * fileE[1]}{'DECRYPTED' * (not fileE[1])}]")
    
    def pushButtonAddFile_Clicked(self) -> None:
        """Load file button in the encrypt/decrypt tab is clicked"""
        fileName = self.getFileName()
        if fileName != "":
            fileExists = False
            for fileE in self.filesToEncrypt: #checking if the file already exists in program
                if fileName == fileE[0]:
                    fileExists = True
                    break
            if fileExists:
                QMessageBox.information(self, 'File Already Stored', "That file already exists. You can not add the same files multiple times, only one instance of the file can exist.", QMessageBox.Ok)
            else: #if the file doesn't exist in the program
                self.filesToEncrypt.append([fileName, False])
                self.updateFilesListWidget()
                accountFunctions.saveFilesToEncrypt(self.filesToEncrypt, self.f)
                self.enableFileOptions()
                self.disableFileOption()
    
    def enableFileOptions(self) -> None:
        """Enable the file options in the encrypt and decrypt file tab"""
        self.pushButtonRemoveFile.setEnabled(True)
        self.groupBoxEncryption.setEnabled(True)
        self.groupBoxEncryption_2.setEnabled(True)
        self.pushButtonRemoveFile.setEnabled(True)
        self.pushButtonAddFile_2.setEnabled(True)
        self.pushButtonAddFile_6.setEnabled(True)
    
    def disableFileOption(self) -> None:
        """Disable some file options based on if there are/aren't files stored in the program"""
        if len(self.filesToEncrypt) > 0:
            self.pushButtonRemoveFile.setEnabled(False)
            self.pushButtonAddFile_2.setEnabled(False)
            self.pushButtonAddFile_6.setEnabled(False)
        else:
            self.pushButtonRemoveFile.setEnabled(False)
            self.groupBoxEncryption.setEnabled(False)
            self.groupBoxEncryption_2.setEnabled(False)
    
    def listWidgetFiles_CurrentRowChanged(self) -> None:
        self.enableFileOptions()
        if len(self.filesToEncrypt) > 0:
            if self.filesToEncrypt[self.listWidgetFiles.currentRow()][1] == True:
                self.pushButtonAddFile_2.setEnabled(False)
                self.pushButtonAddFile_6.setEnabled(True)
            else:
                self.pushButtonAddFile_6.setEnabled(False)
                self.pushButtonAddFile_2.setEnabled(True)
        else:
            self.disableFileOption()

    def pushButtonRemoveFile_Clicked(self) -> None:
        """Remove file path stored in files list widget"""
        removeFile = QMessageBox.question(self, "Remove File?", "Are you sure you want to remove this file from the program?", QMessageBox.Yes, QMessageBox.No)
        if removeFile == QMessageBox.Yes:
            if self.filesToEncrypt[self.listWidgetFiles.currentRow()][1] == True: #if the file is encrypted and user wants to remove it
                accountFunctions.decrypt_file(self.filesToEncrypt[self.listWidgetFiles.currentRow()][0], self.f) #decrypt file before removing it
            self.filesToEncrypt.pop(self.listWidgetFiles.currentRow())
            self.updateFilesListWidget()
            accountFunctions.saveFilesToEncrypt(self.filesToEncrypt, self.f)
            self.disableFileOption()
    
    def pushButtonAddFile_2_Clicked(self) -> None: #encrypting file button pushed
        if self.filesToEncrypt[self.listWidgetFiles.currentRow()][1] == False: #if the file is not encrypted
            currRow = self.listWidgetFiles.currentRow()
            encryptFile = accountFunctions.encrypt_file(self.filesToEncrypt[self.listWidgetFiles.currentRow()][0], self.f)
            fileName = self.filesToEncrypt[self.listWidgetFiles.currentRow()][0].split("/")[-1]
            if encryptFile:
                self.filesToEncrypt[self.listWidgetFiles.currentRow()][1] = True
                self.updateFilesListWidget()
                accountFunctions.saveFilesToEncrypt(self.filesToEncrypt, self.f)
                QMessageBox.information(self, "File Encryption Successful       ", f"Successfully encrypted:\n\n{fileName}")
                self.listWidgetFiles.setCurrentRow(currRow)
            else:
                QMessageBox.information(self, "File not Found", f"The file you want to decrypt could not be found.\n\nPlease ensure that the file is in this directory: {self.filesToEncrypt[self.listWidgetFiles.currentRow()][0]}\n\nWith the name and extension: {fileName}")
    
    def pushButtonAddFile_6_Clicked(self) -> None: #decrypting file button pushed
        if self.filesToEncrypt[self.listWidgetFiles.currentRow()][1] == True: #if the file is encrypted
            currRow = self.listWidgetFiles.currentRow()
            decryptFile = accountFunctions.decrypt_file(self.filesToEncrypt[self.listWidgetFiles.currentRow()][0], self.f)
            fileName = self.filesToEncrypt[self.listWidgetFiles.currentRow()][0].split("/")[-1]
            if decryptFile:
                self.filesToEncrypt[self.listWidgetFiles.currentRow()][1] = False
                self.updateFilesListWidget()
                accountFunctions.saveFilesToEncrypt(self.filesToEncrypt, self.f)
                QMessageBox.information(self, "File Decryption Successful       ", f"Successfully decrypted:\n\n{fileName}")
                self.listWidgetFiles.setCurrentRow(currRow)
            else:
                QMessageBox.information(self, "File not Found", f"The file you want to decrypt could not be found.\n\nPlease ensure that the file is in this directory: {self.filesToEncrypt[self.listWidgetFiles.currentRow()][0]}\n\nWith the name and extension: {fileName}")

    def pushButtonAddFile_3_Clicked(self) -> None: #encrypt all files
        """Encrypt all files button is pressed. Encrypts all files in the list, update list widget, output success message box."""
        if len(self.filesToEncrypt) > 0: #if there are files stored
            stringFilesEncrypted = ""
            stringFilesError = ""
            for fileE in self.filesToEncrypt:
                if fileE[1] == False: #if file to encrypt is not encrypted
                    fileName = fileE[0].split("/")[-1]
                    encryptFile = accountFunctions.encrypt_file(fileE[0], self.f) #if file can't be found
                    if encryptFile == False: #if file is not found
                        QMessageBox.information(self, "File not Found", f"The file you want to encrypt could not be found.\n\nPlease ensure that the file is in this directory: {fileE[0]}\n\nWith the name and extension: {fileName}")
                        stringFilesError += fileName + "\n"
                    else:
                        stringFilesEncrypted += fileName + "\n"
                        fileE[1] = True #change file status to encrypted
            self.updateFilesListWidget()
            accountFunctions.saveFilesToEncrypt(self.filesToEncrypt, self.f)
            if stringFilesEncrypted != "" and stringFilesError == "":
                QMessageBox.information(self, "File Encryption Successful       ", f"Successfully encrypted:\n\n{stringFilesEncrypted}")
            elif stringFilesEncrypted == "" and stringFilesError != "":
                QMessageBox.information(self, "No Files Encrypted       ", f"Could not encrypt the following files:\n\n{stringFilesError}")
            elif stringFilesEncrypted != "" and stringFilesError != "":
                QMessageBox.information(self, "File Encryption Partially Successful       ", f"Successfully encrypted:\n\n{stringFilesEncrypted}\n\nCould not encrypt the following files:\n\n{stringFilesError}")
        else:
            QMessageBox.information(self, "No Files To Encrypt", f"There are currently no files stored in the program to encrypt.")
    
    def pushButtonAddFile_7_Clicked(self) -> None:
        """decrypt all files button is pressed. Encrypts all files in the list, update list widget, output success message box."""
        if len(self.filesToEncrypt) > 0: #if there are files stored
            stringFilesDecrypted = ""
            stringFilesError = ""
            for fileE in self.filesToEncrypt:
                if fileE[1] == True: #if file to encrypt is encrypted
                    fileName = fileE[0].split("/")[-1]
                    decryptFile = accountFunctions.decrypt_file(fileE[0], self.f) #if file can't be found
                    if decryptFile == False: #if file is not found
                        QMessageBox.information(self, "File not Found", f"The file you want to decrypt could not be found.\n\nPlease ensure that the file is in this directory: {fileE[0]}\n\nWith the name and extension: {fileName}")
                        stringFilesError += fileName + "\n"
                    else:
                        stringFilesDecrypted += fileName + "\n"
                        fileE[1] = False #change to not encrypted
            self.updateFilesListWidget()
            accountFunctions.saveFilesToEncrypt(self.filesToEncrypt, self.f)
            self.disableFileOption()
            if stringFilesDecrypted != "" and stringFilesError == "":
                QMessageBox.information(self, "File Decryption Successful       ", f"Successfully decrypted:\n\n{stringFilesDecrypted}")
            elif stringFilesDecrypted == "" and stringFilesError != "":
                QMessageBox.information(self, "No Files Decrypted       ", f"Could not decrypt the following files:\n\n{stringFilesError}")
            elif stringFilesDecrypted != "" and stringFilesError != "":
                QMessageBox.information(self, "File Decrpytion Partially Successful       ", f"Successfully decrypted:\n\n{stringFilesDecrypted}\n\nCould not decrypt the following files:\n\n{stringFilesError}")
        else:
            QMessageBox.information(self, "No files to decrypt", f"There are currently no files stored in the program to decrypt.")


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


class AccountSettingsWindow(QDialog, Ui_AccountSettingsWindow.Ui_Dialog):
    """Account settings dialog window"""

    def __init__(self, parent, accountInfo):
        super().__init__(parent)
        self.setupUi(self)
        self.labelPasswordWarning.hide()
        self.labelSecurityQuestion1Warning.hide()
        self.labelSecurityQuestion2Warning.hide()
        self.accountInfo = accountInfo #account info structure -> {"username": None, "email": None, "password": None, "SQuestion1": None, "SAnswer1": None, "SQuestion2" : None, "SAnswer2" : None}
        self.setUpInfo()
        self.tabWidgetAccountInformation.setCurrentIndex(0)
        self.changesMade = False
        #signals
        self.pushButtonEditInfo.clicked.connect(self.pushButtonEditInfo_Clicked) #edit account info button clicked
        self.pushButtonEditQuestions.clicked.connect(self.pushButtonEditQuestions_Clicked)
        self.tabWidgetAccountInformation.currentChanged.connect(self.tabWidgetAccountInformation_CurrentChanged)
        self.pushButtonViewPassword.clicked.connect(self.pushButtonViewPassword_Clicked)
        self.pushButtonHidePassword.clicked.connect(self.pushButtonHidePassword_Clicked)
        #saving
        self.pushButtonSaveChanges.clicked.connect(self.pushButtonSaveChanges_Clicked)
        self.pushButtonSaveChanges_2.clicked.connect(self.pushButtonSaveChanges_2_Clicked)
    
    def setUpInfo(self) -> None:
        """Set up the information in the account information tab, security questions tab, and resetting read only property and password to secure string"""
        #account info
        self.lineEditUsername.setText(self.accountInfo["username"])
        self.lineEditPassword.setText(self.accountInfo["password"])
        self.lineEditPasswordConfirm.setText(self.accountInfo["password"])
        self.lineEditEmail.setText(self.accountInfo["email"])
        self.lineEditUsername.setReadOnly(True)
        self.lineEditPassword.setReadOnly(True)
        self.lineEditPasswordConfirm.setReadOnly(True)
        self.lineEditEmail.setReadOnly(True)
        self.pushButtonSaveChanges.setEnabled(False)
        self.pushButtonEditInfo.setEnabled(True)
        self.pushButtonHidePassword_Clicked()
        #security questions
        self.lineEditQuestion1.setText(self.accountInfo["SQuestion1"])
        self.lineEditAnswer1.setText(self.accountInfo["SAnswer1"])
        self.lineEditQuestion2.setText(self.accountInfo["SQuestion2"])
        self.lineEditAnswer2.setText(self.accountInfo["SAnswer2"])
        self.lineEditQuestion1.setReadOnly(True)
        self.lineEditAnswer1.setReadOnly(True)
        self.lineEditQuestion2.setReadOnly(True)
        self.lineEditAnswer2.setReadOnly(True)
        self.pushButtonEditQuestions.setEnabled(True)
        self.pushButtonSaveChanges_2.setEnabled(False)
    
    def pushButtonEditInfo_Clicked(self) -> None:
        self.lineEditUsername.setReadOnly(False)
        self.lineEditPassword.setReadOnly(False)
        self.lineEditPasswordConfirm.setReadOnly(False)
        self.lineEditEmail.setReadOnly(False)
        self.pushButtonSaveChanges.setEnabled(True)
        self.pushButtonEditInfo.setEnabled(False)
    
    def pushButtonEditQuestions_Clicked(self) -> None:
        self.lineEditQuestion1.setReadOnly(False)
        self.lineEditAnswer1.setReadOnly(False)
        self.lineEditQuestion2.setReadOnly(False)
        self.lineEditAnswer2.setReadOnly(False)
        self.pushButtonEditQuestions.setEnabled(False)
        self.pushButtonSaveChanges_2.setEnabled(True)
    
    def tabWidgetAccountInformation_CurrentChanged(self) -> None:
        self.setUpInfo()
        self.labelSecurityQuestion1Warning.hide()
        self.labelSecurityQuestion2Warning.hide()
        self.labelPasswordWarning.hide()
    
    def pushButtonViewPassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.EchoMode.Normal)
    
    def pushButtonHidePassword_Clicked(self) -> None:
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEditPasswordConfirm.setEchoMode(QLineEdit.EchoMode.Password)
    
    def pushButtonSaveChanges_Clicked(self) -> None:
        """Save the changes made to the account information tab"""
        if self.lineEditPassword.text() == self.lineEditPasswordConfirm.text(): #if passwords match
            if len(self.lineEditPassword.text()) >= 8: #if password is 8 or more characters
                self.accountInfo["username"] = self.lineEditUsername.text()
                self.accountInfo["password"] = self.lineEditPassword.text()
                self.accountInfo["email"] = self.lineEditEmail.text()
                self.changesMade = True
                QMessageBox.information(self, "Account information Changed", "Account informtion has been changed. Please close the account settings window to ensure that the changes made are saved in the program.", QMessageBox.Ok)
                self.labelPasswordWarning.hide()
                self.setUpInfo()
            else:
                self.labelPasswordWarning.setText("Password is not 8 characters")
                self.labelPasswordWarning.show()
        else:
            self.labelPasswordWarning.setText("Passwords do not match")
            self.labelPasswordWarning.show()
    
    def pushButtonSaveChanges_2_Clicked(self) -> None:
        """Save the changes made to the security questions tab"""
        if self.lineEditQuestion1.text() != "" and self.lineEditAnswer1.text() != "":
            if self.lineEditQuestion2.text() != "" and self.lineEditAnswer2.text() != "":
                self.accountInfo["SQuestion1"] = self.lineEditQuestion1.text()
                self.accountInfo["SAnswer1"] = self.lineEditAnswer1.text()
                self.accountInfo["SQuestion2"] = self.lineEditQuestion2.text()
                self.accountInfo["SAnswer2"] = self.lineEditAnswer2.text()
                self.changesMade = True
                QMessageBox.information(self, "Account Security Questions Changed", "Account security questions have been changed. Please close the account settings window to ensure that the changes made are saved in the program.", QMessageBox.Ok)
                self.labelSecurityQuestion1Warning.hide()
                self.labelSecurityQuestion2Warning.hide()
                self.setUpInfo()
            else:
                self.labelSecurityQuestion2Warning.setText("Security Question/Answer is blank")
                self.labelSecurityQuestion2Warning.show()
        else:
            self.labelSecurityQuestion1Warning.setText("Security Question/Answer is blank")
            self.labelSecurityQuestion1Warning.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = AccountHolder()
#     window.show()
#     sys.exit(app.exec_())