from cryptography.fernet import Fernet
import pickle, os, time

# ox01.txt holds key
# ox02.pkl holds account info
#ox03.pkl hold all the accounts

def generateKey() -> str:
    """Generate key"""
    key = Fernet.generate_key() #generate a key
    with open("ox01.txt", "wb") as key_file: #writing the key to a text file
        key_file.write(key)
    return key

def saveUserAccountInfo(accountInfoDict : dict, f) -> None:
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