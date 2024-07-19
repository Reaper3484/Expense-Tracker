import json
import os


def is_empty(obj):
    empty=False
    if obj=='':
        empty=True
    return empty

def pass_length(password):
    if len(password)==6:
        return True
    

def register():
    with open('Data.json','r') as Data:
        user=json.load(Data)
    name=''
    username=''
    pwd=''   
    VALID = True
    CORRECT = True
    while CORRECT:
        name = input("Enter your name : ")
        if is_empty(name):
            print("Please Enter a Name and then continue : ")
            continue
        username = input("Choose a username : ")
        if is_empty(username):
            print("Please Enter a Username and then continue : ")
            continue
        pwd=input("Type in a 6-digit Password : ")
        if is_empty(pwd):
            print("Please Enter a Password and then continue : \n")
            continue
        elif not pass_length(pwd):
            print("Password should be 6 characters Long")
            continue
        VALID = True

        for i in user['users']:
            if i['username'] ==username:
                VALID=False
                CORRECT=True
                print("That username is already taken. Please Try Again!!!")
                retry = input("do you want to retry : Y/N : ")
                if retry.upper()=='Y':
                    break
                elif retry.upper()=='N':
                    print("THANK YOU !!!")
                    break
                else:
                    print("Not a Valid Input")
        if VALID:
            break  
        
    if VALID:
        user['users'].append({
            'name': name,
            'username':username,
            'pwd': pwd
            })

    with open('Data.json','w') as Data:
        json.dump(user, Data, indent=4)

    