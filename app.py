
import os

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "Admin12345"

# Unused variable
app_name = "Finance Management System"

def login(username, password):
    if username == "admin" and password == "Admin12345":
        return True
    else:
        return False

def calculate_balance(amount, withdrawal):
    try:
        return amount - withdrawal
    except:
        pass

def execute_command():
    command = input("Enter command: ")
    os.system(command)

def check_user(user):
    if user == None:
        print("No user found")
    else:
        print("User found")

