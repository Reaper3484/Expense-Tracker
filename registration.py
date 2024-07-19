import json
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_empty(obj):
    return obj == ''

def pass_length(password):
    return len(password) == 6

def register():
    
    with open('Data.json', 'r') as Data:
        user = json.load(Data)
    
    name = ''
    username = ''
    pwd = ''
    VALID = True
    CORRECT = True
    
    while CORRECT:
        clear()  
        name = input("Enter your name: ")
        if is_empty(name):
            print("Please Enter a Name and then continue.")
            input("Press Enter to continue...")  
            continue
        
        clear()  
        username = input("Choose a username: ")
        if is_empty(username):
            print("Please Enter a Username and then continue.")
            input("Press Enter to continue...")
            continue
        
        clear()  
        pwd = input("Type in a 6-digit Password: ")
        if is_empty(pwd):
            print("Please Enter a Password and then continue.")
            input("Press Enter to continue...")
            continue
        elif not pass_length(pwd):
            print("Password should be 6 characters Long.")
            input("Press Enter to continue...")
            continue
        
        VALID = True
        for i in user['users']:
            if i['username'] == username:
                VALID = False
                CORRECT = True
                print("That username is already taken. Please Try Again!!!")
                retry = input("Do you want to retry: Y/N: ")
                if retry.upper() == 'Y':
                    break
                elif retry.upper() == 'N':
                    print("THANK YOU!!!")
                    return
                else:
                    print("Not a Valid Input.")
                    input("Press Enter to continue...")
        
        if VALID:
            break
    
    if VALID:
        user['users'].append({
            'name': name,
            'username': username,
            'pwd': pwd
        })
    
    with open('Data.json', 'w') as Data:
        json.dump(user, Data, indent=4)
    
    print("Registration Successful!")
