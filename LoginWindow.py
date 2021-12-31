import sys, random
from cryptography.fernet import Fernet
from PyQt5.QtCore import QFile, QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
import accountFunctions
import emailRecoverySend
import Ui_LoginWindow
import Ui_SecurityQuestion
import Ui_ChangePassword
import Ui_EmailSecurityCodeRecovery

class LoginWindow(QMainWindow, Ui_LoginWindow.Ui_MainWindow):
    """Login Window"""
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.labelIncorrectInfo.hide()
        self.loginSuccess = False
        #account info
        self.accountInfo = None #structure -> {"username": None, "email": None, "password": None, "SQuestion1": None, "SAnswer1": None, "SQuestion2" : None, "SAnswer2" : None}
        self.f = None
        self.key = None
        self.getKey()
        self.getAccountInfo()
        #account recovery
        self.accountRecoveryQuestionChoice = str(random.randint(1, 2)) #choose between question 1 or 2
        #signals
        self.pushButtonLogin.clicked.connect(self.pushButtonLogin_Clicked)
        self.pushButtonRecoverAccount.clicked.connect(self.pushButtonRecoverAccount_Clicked)
    
    def pushButtonRecoverAccount_Clicked(self):
        popSQuestion = SecurityQuestion(self.accountInfo[f"SQuestion{self.accountRecoveryQuestionChoice}"], self.accountInfo[f"SAnswer{self.accountRecoveryQuestionChoice}"], self)
        popSQuestion.show()
        popSQuestion.exec_() #allow following lines of code to execute from pop up menu, this code is used to transition between windows and widgets
        if popSQuestion.success: #if security question was successfully answered
            code = "".join([str(random.randint(0,9)) for i in range(9)])
            popSecurityCodeDialog = EmailSecurityCode(self, code, self.accountInfo["username"], self.accountInfo["email"])
            popSecurityCodeDialog.show()
            popSecurityCodeDialog.exec_()
            if popSecurityCodeDialog.success: #if security code was successfully entered
                popChangePassword = ChangePassword(self)
                popChangePassword.show()
                popChangePassword.exec_()
                if popChangePassword.success:
                    self.accountInfo["password"] = popChangePassword.newPassword
                    accountFunctions.saveUserAccountInfo(self.accountInfo, self.f)
    
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
    
    def pushButtonLogin_Clicked(self):
        if all([self.checkUserName(), self.checkPassword()]):
            self.labelIncorrectInfo.hide()
            QMessageBox.information(self, "Successfully logged in", "Login is successful, welcome.")
            self.loginSuccess = True
            self.close()
        else:
            self.labelIncorrectInfo.show()

    def checkUserName(self) -> bool:
        if self.lineEditUsername.text() == self.accountInfo["username"]:
            return True
        else:
            return False

    def checkPassword(self) -> bool:
        if self.lineEditPassword.text() == self.accountInfo["password"]:
            return True
        else:
            return False

class SecurityQuestion(QDialog, Ui_SecurityQuestion.Ui_Dialog):
    """Security question dialog window for account recovery"""

    def __init__(self, question, answer, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.labelQuestion.setText(question)
        self.label.hide()
        self.answer = answer
        self.success = False
        #signals
        self.pushButtonEnterAnswer.clicked.connect(self.pushButtonEnterAnswer_Clicked)
    
    def pushButtonEnterAnswer_Clicked(self):
        if self.lineEdit.text().lower() == self.answer.lower():
            self.label.hide()
            QMessageBox.information(self, "Security Question Successful", "Security answer is correct, please continue with account recovery.", QMessageBox.Ok)
            self.success = True
            self.close()
        else:
            self.label.show()
    
class ChangePassword(QDialog, Ui_ChangePassword.Ui_Dialog):
    """Change Password dialog window"""

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.label.hide()
        self.newPassword = None
        self.success = False
        #signals
        self.pushButtonChangePassword.clicked.connect(self.pushButtonChangePassword_Clicked)
    
    def pushButtonChangePassword_Clicked(self):
        if len(self.lineEditPassword.text()) < 8 or len(self.lineEditPasswordConfirm.text()) < 8:
            self.label.setText("Password has to be 8 characters")
            self.label.show()
        else:
            if self.lineEditPassword.text() != self.lineEditPasswordConfirm.text(): #if passwords do not match
                self.label.setText("Passwords do not match!")
            else:
                self.label.hide()
                self.newPassword = self.lineEditPassword.text()
                QMessageBox.information(self, "Password Change Success", "Password was successfully changed. You can now login with the your new password")
                self.success = True
                self.close()

class EmailSecurityCode(QDialog, Ui_EmailSecurityCodeRecovery.Ui_Dialog):
    """Enter security codes sent to user email"""
    def __init__(self, parent, code : str, username : str, emailAddress : str):
        super().__init__(parent)
        self.code = code
        self.username = username
        self.emailAddress = emailAddress
        self.sendEmailCode() #send the code to the email address of the user
        self.success = False
        self.setupUi(self)
        self.labelIncorrectCode.hide()
        #signals
        self.pushButton.clicked.connect(self.pushButton_Clicked)
    
    def sendEmailCode(self):
        try:
            emailRecoverySend.sendEmail(self.code, self.emailAddress, self.username)
        except:
            QMessageBox.information(self, "Error", "An error ocurred when attempting to send the security code, please ensure that you are connected to the internet and try again.")
    
    def pushButton_Clicked(self):
        if self.lineEdit.text() == self.code:
            self.labelIncorrectCode.hide()
            QMessageBox.information(self, "Security Code Correct", "Security code entered is correct, please continue with account recovery.", QMessageBox.Ok)
            self.success = True
            self.close()
        else:
            self.labelIncorrectCode.setText("Code is incorrect.")
            self.labelIncorrectCode.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
