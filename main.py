from cryptography.fernet import Fernet, InvalidToken
from time import sleep
import datetime
import h5py
import sys
import os
import bcrypt

author = "Gokul B"

class Main_Func:
    """
    In this class include every important function which make the register and login secure
    Like encryption, decryption, hashing password and matching the hashed password
    """
    def __init__(self):
        pass
    def encryption(self, username, password, name):  #This used to encrypt the hashed password
        key = Fernet.generate_key()
        #encoded_passw = password.encode()
        cipher_suit = Fernet(key)
        encrypted_passw = cipher_suit.encrypt(password)
        with h5py.File('user_key.h5', 'a') as file2: # This is where the key are stored in the file
            group = file2.create_group(username)
            group.attrs['name'] = name
            group.attrs['key'] = key
        return encrypted_passw

    def decryption(self, username):
        with h5py.File('user_details.h5', 'r') as file3: ## Checking if the user in registered and collecting the encrypted password
            if username in file3:
                group = file3[username]
                password = group.attrs['password']
                with h5py.File('user_key.h5', 'r') as file4: ## Checking if the user key is saved in the user_key and collecting the key
                    groups = file4[username]
                    key = groups.attrs['key']
                    cipher_suit = Fernet(key)
                    d_password = cipher_suit.decrypt(password)
                    #decoded_passw = decrypted_password.decode()
        return d_password # Returning the decoded password or the hashed password

    def hashing_pass(self, password):
        salt = bcrypt.gensalt()
        hashed_passw = bcrypt.hashpw(password.encode('utf8'), salt)
        return hashed_passw, salt


    def matching_hash(self, password, decrypted_password):
        entred_password = password.encode('utf8')
        if bcrypt.checkpw(entred_password, decrypted_password):
            return 1
        else:
            return 0

class Save_In_Database:
    """
    This class is used to make the proper saving user data in the database
    """
    def register_data(self,username, name, password, status, dob):
        try:
            hashed_passw, salt = mainfunc.hashing_pass(password)
            encrypted_password = mainfunc.encryption(username, hashed_passw, name)
            with h5py.File('user_details.h5', 'a') as file:
                group = file.create_group(username)
                group.attrs['name'] = name
                group.attrs['salt'] = salt
                group.attrs['password'] = encrypted_password
                group.attrs['status'] = status
                group.attrs['dob'] = dob
                logfunc.register_log(username)
                return 1
        except:
            print("The Username is already exists!")
            return 0

class Display:
    """
    This class print the data given by the user for the confirmation for the registration and etc
    """
    def confirm_registration(self, username, password, name, status, dob): #This function is used to see the user data they entered in
        len_pass = len(password)
        star_sign = len_pass * "*"
        print('\n')
        print(f"Your Username: {username}")
        print(f"Your Password: {star_sign}")
        print(f"Your Name:     {name}")
        print(f"Your Status:   {status}")
        print(f"Your DOB:      {dob}")
        sleep(3)
        print('\n')

class User_Input:
    """
    This class handle the all user inputs in the registration and login process
    """
    def register_input(self): #Collecting the details for registering new user in the database
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        status = input("Enter Your Status: ")
        dob = int(input("Enter Your DOB: "))
        return username, password, name, status, dob

    def login_input(self): #Collecting the details for login
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        return username, password

class Log_Func:
    """
    This class contain the function that are capable for the saving both registration and login log in files
    """
    def __init__(self):
        now = datetime.datetime.now()
        self.exact_time = now.strftime("%Y-%m-%d %H:%M:%S") #This value of the var is the year-month-day hour:minute:second

    def register_log(self, username):  #This function is used to save the registred log in a file
        log_entry = f"{self.exact_time} Username: {username}"
        with open('register_log.txt', 'a', encoding='utf8') as reg_log:
            reg_log.write(log_entry)

    def login_log(self, username): #Thiss function is used to save the login log in a file
        log_entry = f"{self.exact_time} Username: {username}"
        with open('login_log.txt', 'a', encoding='utf8') as loged_log:
            loged_log.write(log_entry)

class Execute:
    """
    This class collect all the info from other class and combine to work proper registration and login process
    """
    def register(self):
        while True:
            username, password, name, status, dob = userinput.register_input()
            display.confirm_registration(username, password, name, status, dob)
            confirm = input("Do You Want To Proceed The Registeration(yes/no):  ")
            if confirm == 'yes': #This is were register function are executed
                checkerror = saveindatabase.register_data(username, name, password, status, dob)
                if checkerror == 1:
                    sleep(3)
                    print('\n')
                    print('You are successfully Registred in ......./')
                    return 1
                    break
                elif checkerror == 0:
                    print("Restarting from the begining")
            elif confirm == 'no':
                print("It's time to say Good Byes.....")
                sleep(3)
                sys.exit()

    def login(self):
        username, password = userinput.login_input()
        decrypted_password = mainfunc.decryption(username)
        passw_check = mainfunc.matching_hash(password, decrypted_password)
        if passw_check == 1:
            print("You are successfully loged in ")
            return 1
        elif passw_check == 0:
            print("The Password is wrong.....")
            return 0

class Handle_error_loop:
    """
    This class contain function that make sure registration and login are in a loop to prevent the termination of the code
    """
    def main_loop(self):
        while True:
            type = input("Do you want register or login (r/l): ")
            if type == 'r':
                check_error_register = execute.register()
                if check_error_register == 1: #This will entred to the loop if the register fuction is completed without the error
                    pass
            elif type == 'l':
                check_login = execute.login()
                if check_login == 1:
                    logfunc.login_log(username) #Store the login log in the file
                    break
                elif check_login == 0:
                    pass

            else:
                print("Wrong input! Restart the application")
                print('\n')


if __name__ == '__main__':
    userinput = User_Input()
    display = Display()
    mainfunc = Main_Func()
    saveindatabase = Save_In_Database()
    execute = Execute()
    handleerrorloop = Handle_error_loop()
    logfunc = Log_Func()
    handleerrorloop.main_loop()
