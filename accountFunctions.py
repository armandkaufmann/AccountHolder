from cryptography.fernet import Fernet
import pickle, os, time

# ox01.txt holds key
# ox02.pkl holds account info
#ox03.pkl hold all the accounts
#ox04.pkl hold all the encrypted file info sturcutre -> [['filePath', True or False (True for encrypted)]]

def generateKey() -> str:
    """Generate key"""
    key = Fernet.generate_key() #generate a key
    with open("ox01.txt", "wb") as key_file: #writing the key to a text file
        key_file.write(key)
    return key

def loadKey() -> str:
    """Loads key from file, returns the key"""
    key = None
    with open("ox01.txt", "rb") as key_file:
        key = key_file.read()
    return key

def saveUserAccountInfo(accountInfoDict : dict, f : object) -> None:
    """Saves the user account info, and encrypt the file"""
    with open("ox02.pkl", "wb") as account_info:
        pickle.dump(accountInfoDict, account_info)
    encrypt_file("ox02.pkl", f)

def loadUserAccountInfo(f : object) -> dict:
    """Return decrypted user account info"""
    accountInfo = None
    decrypt_file("ox02.pkl", f)
    with open("ox02.pkl", "rb") as account_info:
        accountInfo = pickle.load(account_info)
    encrypt_file("ox02.pkl", f)
    return accountInfo

def loadUserAccounts(f : object) -> dict:
    """Return decrypted user stored accounts"""
    accounts = None
    decrypt_file("ox03.pkl", f)
    with open("ox03.pkl", "rb") as account_info:
        accounts = pickle.load(account_info)
    encrypt_file("ox03.pkl", f)
    return accounts

def saveUserAccounts(accounts : list, f : object) -> dict:
    """save user accounts as a pickle file, and encrypt file"""
    with open("ox03.pkl", "wb") as accountsFile:
        pickle.dump(accounts, accountsFile)
    encrypt_file("ox03.pkl", f)

def checkAccountFileExist() -> bool:
    """Check if the file that holds the account exists, returns bool based on that."""
    try:
        with open("ox03.pkl", "rb") as f:
            f.read()
    except FileNotFoundError:
        return False
    else:
        return True

#File Encryption funcions
def checkFileToEncryptExist(filePath : str) -> bool:
    """Checks if the file to encrpypt or decrpyt exists"""
    try:
        with open(filePath, "rb") as f:
            f.read()
    except FileNotFoundError:
        return False
    else:
        return True

def saveFilesToEncrypt(filesList : list, f : object) -> None:
    """save user accounts as a pickle file, and encrypt file"""
    with open("ox04.pkl", "wb") as encryptFileList:
        pickle.dump(filesList, encryptFileList)
    encrypt_file("ox04.pkl", f)

def loadFilesToEncryptList(f : object) -> list:
    """Decrypt files to encrypt list and encrypt once done loading. Retures list of files to encrypt."""
    accounts = None
    decrypt_file("ox04.pkl", f)
    with open("ox04.pkl", "rb") as account_info:
        accounts = pickle.load(account_info)
    encrypt_file("ox04.pkl", f)
    return accounts

def encrypt_file(filename : str, f : object):
    with open(filename, 'rb') as file_target:
        file_data = file_target.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file_target:
        file_target.write(encrypted_data)
        
def decrypt_file(filename : str, f : object):
    with open(filename, 'rb') as file_target:
        file_data = file_target.read()
    decrypted_data = f.decrypt(file_data)
    with open(filename, 'wb') as file_target:
        file_target.write(decrypted_data)
