import sys, random
from cryptography.fernet import Fernet
from PyQt5.QtCore import QFile, QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QLineEdit, QMainWindow, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
import AccountHolder
import CreateAccount
import LoginWindow
import accountFunctions

def createAccountRun() -> bool:
    """Run the create account window"""
    app = QApplication(sys.argv)
    window = CreateAccount.CreateAccountWindow()
    window.show()
    app.exec_()
    return window.success

def loginWindowRun() -> bool:
    """Run the login window"""
    app = QApplication(sys.argv)
    window = LoginWindow.LoginWindow()
    window.show()
    app.exec_()
    return window.loginSuccess

def accountHolderRun() -> bool:
    """Run the account holder application"""
    app = QApplication(sys.argv)
    window = AccountHolder.AccountHolder()
    window.show()
    sys.exit(app.exec_())

def main() -> None:
    """Runs the program"""
    if not accountFunctions.checkAccountExist(): #if the account file doesn't exist
        createAcc = createAccountRun()
        if createAcc:
            loginW = loginWindowRun()
            if loginW:
                accountHolderRun()
    else:
        loginW = loginWindowRun()
        if loginW:
            accountHolderRun()

if __name__ == "__main__":
    main()




