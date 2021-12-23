from cryptography.fernet import Fernet
import pickle, os, time

def create_username(key, f):
    """
    creates the user's username, and stores it in encrypted file
    """
    function_run = True
    while function_run:
        username = input("\nPlease enter your username: ")
        while True:
            question = input(f"\nAre you sure you want the username:[{username}]? ('yes' or 'no'): ")
            if question == 'no':
                break
            elif question == 'yes':
                function_run = False
                break
            else:
                print("Please enter a valid input!")
                continue
        if function_run:
            continue
    os.system('cls' if os.name == 'nt' else 'clear')
    encrypted_username = f.encrypt(username.encode())
    with open('master_username.txt', 'wb') as file_target:
        file_target.write(encrypted_username)

    return username


def initialize_new_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    return key

def create_new_password(key, f):
    """Generates password"""
    while True:
        password1 = input('\nPlease choose a master password to secure your accounts (Password is case-sensitive): ')
        password2 = input('\nPlease re-enter your password: ')
        if password1 != password2:
            print("\nYour passwords did not match, please re-enter the password!")
            continue
        elif password1 == password2:
            print("\nYour password has been recorded, please remember your password!")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break

    encrypted_password = f.encrypt(password1.encode())
    with open('master_password.txt', 'wb') as file_target:
        file_target.write(encrypted_password)

    return password1

def load_key():
    """
    loads the key
    """
    with open('key.key', 'rb') as f:
        key = f.read()
    return key

def load_password(f):
    """
    loads the user's password
    """
    with open('master_password.txt', 'rb') as file_target:
        password = f.decrypt(file_target.read())
    return password.decode()

def load_username(f):
    """
    loads the user's username
    """
    with open('master_username.txt', 'rb') as file_target:
        username = f.decrypt(file_target.read())
    return username.decode()

def encrypt_file(filename, key, f):
    with open(filename, 'rb') as file_target:
        file_data = file_target.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file_target:
        file_target.write(encrypted_data)
        
def decrypt_file(filename, key, f):
    with open(filename, 'rb') as file_target:
        file_data = file_target.read()
    decrypted_data = f.decrypt(file_data)
    with open(filename, 'wb') as file_target:
        file_target.write(decrypted_data)