import sys
from cryptography.fernet import Fernet
from PyQt5.QtCore import QFile, QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QPixmap
import accountFunctions
import Ui_LoginWindow

class CreateAccountWindow(QMainWindow, Ui_LoginWindow.Ui_MainWindow):
    """Create account Window"""
    def __init__(self, parent=None):
        super(CreateAccountWindow, self).__init__(parent)
        self.setupUi(self)
        self.labelPasswordMatchIcon.hide()
        self.labelPasswordMatch.hide()
        self.labelNameIcon.hide()
        self.labelSecurityQuestion1Icon.hide()
        self.labelSecurityQuestion2Icon.hide()
        #user info
        self.userInfo = {"username": None, "password": None, "SQuestion1": None, "SAnswer1": None, "SQuestion2" : None, "SAnswer2" : None}
        self.key = None
        self.f = None
        #signals
        self.pushButtonCreateAccount.clicked.connect(self.pushButtonCreateAccount_Clicked)
    
    def pushButtonCreateAccount_Clicked(self):
        noEmptyInput = self.checkAllFields()
        if noEmptyInput: #no missing information
            passwordMatch = self.checkPasswordMatch()
            if passwordMatch: #if passwords match
                self.labelPasswordMatchIcon.hide()
                self.labelPasswordMatch.hide()
                passwordMinLength = self.checkPasswordLength()
                if passwordMinLength: #if password is 8 characters long
                    self.setUpAccount()
                else: #password is less than 8 character
                    self.labelPasswordMatch.setText("Password is not 8 characters")
                    self.labelPasswordMatchIcon.show()
                    self.labelPasswordMatch.show()
            else: #passwords do not match
                self.labelPasswordMatch.setText("Passwords do not match")
                self.labelPasswordMatchIcon.show()
                self.labelPasswordMatch.show()
        else: #if there is missing information
            QMessageBox.information(self, "Missing account information", "Please ensure that all the set-up information is filled out before clicking create account!", QMessageBox.Ok)
    
    def setUpAccount(self):
        self.key = accountFunctions.generateKey()
        self.f = Fernet(self.key)
        self.labelPasswordMatchIcon.hide()
        self.labelPasswordMatch.hide()
        self.userInfo["username"] = self.lineEditUserName.text().title()
        self.userInfo["password"] = self.lineEditPassword.text()
        self.userInfo["SQuestion1"] = self.lineQuestion1.text()
        self.userInfo["SAnswer1"] = self.lineAnswer1.text()
        self.userInfo["SQuestion2"] = self.lineQuestion2.text()
        self.userInfo["SAnswer2"] = self.lineAnswer2.text()
        accountFunctions.saveUserAccountInfo(self.userInfo, self.f)
        QMessageBox.information(self, "Success!", "Successfully created account.")
        self.close() #close window

    def checkPasswordMatch(self) -> bool:
        """Checks if the passwords match"""
        if self.lineEditPassword.text() == self.lineEditConfirmPassword.text() and self.lineEditConfirmPassword.text() != "":
            return True
        elif self.lineEditPassword.text() == "" or  self.lineEditConfirmPassword.text() == "":
            self.labelPasswordMatch.setText("Missing password fields")
            self.labelPasswordMatchIcon.show()
            self.labelPasswordMatch.show()
            return False
        else:
            return False
    
    def checkPasswordLength(self) -> bool:
        if len(self.lineEditPassword.text()) >= 8:
            return True
        else:
            return False
    
    def checkAllFields(self) -> bool:
        """Checking if all the input fields have been filled in, return 1 for all filled in 0 for missing fields"""
        missing_info = 1
        if self.lineEditUserName.text() == "":
            self.labelNameIcon.show()
            missing_info = 0
        else:
            self.labelNameIcon.hide()
        if self.lineQuestion1.text() == "":
            self.labelSecurityQuestion1Icon.show()
            missing_info = 0
        else:
            self.labelSecurityQuestion1Icon.hide()
        if self.lineAnswer1.text() == "":
            missing_info = 0
            self.labelSecurityQuestion1Icon.show()
        else:
            self.labelSecurityQuestion1Icon.hide()
        if self.lineQuestion2.text() == "":
            missing_info = 0
            self.labelSecurityQuestion2Icon.show()
        else:
            self.labelSecurityQuestion2Icon.hide()
        if self.lineAnswer2.text() == "":
            missing_info = 0
            self.labelSecurityQuestion2Icon.show()
        else:
            self.labelSecurityQuestion2Icon.hide()
        if self.lineEditPassword.text() == "" or self.lineEditConfirmPassword.text() == "":
            missing_info = 0
            self.labelPasswordMatchIcon.show()
            self.labelPasswordMatch.setText("Missing password fields")
            self.labelPasswordMatch.show()
        else:
            self.labelPasswordMatchIcon.hide()
            self.labelPasswordMatch.hide()
        return missing_info
    
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateAccountWindow()
    window.show()
    sys.exit(app.exec_())