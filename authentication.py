import json  
import hashlib  
import os  
import uuid  
from hi import register_shop
  
# File to store user data  
accounts_file = 'accounts.json'  
  
# Load existing accounts from the file  
def load_accounts():  
    if os.path.exists(accounts_file):  
        with open(accounts_file, 'r') as file:  
            try:  
                accounts = json.load(file)  
            except json.JSONDecodeError:  
                accounts = {}  
    else:  
        accounts = {}  
    return accounts  
  
# Save accounts to the file  
def save_accounts(accounts):  
    with open(accounts_file, 'w') as file:  
        json.dump(accounts, file, indent=4)  
  
# Simple salting and hashing function  
def hash_password(password, salt=None):  
    if salt is None:  
        salt = uuid.uuid4().hex  
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest(), salt  
  
# Sign-up function  
def signup():  
    accounts = load_accounts()  
    email = input("Enter your email: ")  
    if email in accounts:  
        print("An account with this email already exists.")  
        return  
    password = input("Enter your password: ")  
    # Hashing password with salt  
    hashed_password, salt = hash_password(password)  
    account_type = input("Are you signing up as a 'user' or 'merchant'? ")  
    # Save account details  
    accounts[email] = {  
        'password': hashed_password,  
        'salt': salt,  
        'type': account_type  
    }  
    save_accounts(accounts)  
    print("Sign-up successful!")  
  
# Login function  
def login():  
    accounts = load_accounts()  
    email = input("Enter your email: ")  
    password = input("Enter your password: ")  
    account = accounts.get(email)  
    if account:  
        hashed_password, _ = hash_password(password, account['salt'])  
        if hashed_password == account['password']:  
            print(f"Login successful! You are logged in as a {account['type']}.") 
            product=(input("Do you want to add your products :1 or 0 "))
            if(product=="1"):
                register_product()
            return  
    print("Invalid email or password.")  
  
# register product if user is merchant 
def register_product():
    register_shop()
# Main function to handle the user interface  
def main():  
    while True:  
        action = input("Do you want to 'signup' or 'login' or 'exit'? ").lower()  
        if action == 'signup':  
            signup()  
        elif action == 'login':  
            login()  
        elif action == 'exit':  
            break  
        else:  
            print("Invalid option. Please choose 'signup', 'login', or 'exit'.")  
  
if __name__ == "__main__":  
    main()  