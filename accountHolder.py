import sys
from PyQt5.QtCore import QFile, QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QPixmap
import accountFunctions
import Ui_LoginWindow

class LoginWindow(QMainWindow, Ui_LoginWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.labelPasswordMatchIcon.hide()
        self.labelPasswordMatch.hide()
        self.labelNameIcon.hide()
        self.labelSecurityQuestion1Icon.hide()
        self.labelSecurityQuestion2Icon.hide()
        #user info
        self.userName = None
        self.password = None
        self.securityQuestion1 = None
        self.securityAnswer1 = None
        self.securityQuestion2 = None
        self.securityAnswer2 = None
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
                    self.labelPasswordMatchIcon.hide()
                    self.labelPasswordMatch.hide()
                    self.userName = self.lineEditUserName.text().title()
                    self.password = self.lineEditPassword
                    self.securityQuestion1 = self.lineQuestion1
                    self.securityAnswer1 = self.lineAnswer1
                    self.securityQuestion2 = self.lineQuestion2
                    self.securityAnswer2 = self.lineAnswer2
                else: #password is less than 8 character
                    self.labelPasswordMatch.setText("Password is not 8 characters")
                    self.labelPasswordMatchIcon.show()
                    self.labelPasswordMatch.show()
            else: #passwords do not match
                self.labelPasswordMatch.setText("Passwords do not match")
                self.labelPasswordMatchIcon.show()
                self.labelPasswordMatch.show()
        else: #if there is missing information
            QMessageBox.information(self, "Missing account information", "Please ensure that all the set-up information is filled out!", QMessageBox.Ok)


    def checkPasswordMatch(self):
        """Checks if the passwords match"""
        if self.lineEditPassword.text() == self.lineEditConfirmPassword.text() and self.lineEditConfirmPassword.text() != "":
            return True
        elif self.lineEditPassword.text() == "" or  self.lineEditConfirmPassword.text() == "":
            self.labelPasswordMatch.setText("Enter a Password")
            self.labelPasswordMatchIcon.show()
            self.labelPasswordMatch.show()
            return False
        else:
            return False
    
    def checkPasswordLength(self):
        if len(self.lineEditPassword.text()) >= 8:
            return True
        else:
            return False
    
    def checkAllFields(self):
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
        return missing_info

        
    


class MainProgram():

    def __init__(self) -> None:
        self.loggedIn = False
        self.logInAttempts = 0
    
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())