import json


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
        username = input("Choose a username : ")
        pwd=input("Type in a 6-digit Password : ")
    
        VALID = True

        for i in user['users']:
            if i['username'] ==username:
                VALID=False
                CORRECT=True
                print("That username is already taken. Please Try Again!!!")
                retry = input("do you want to retry : Y/N : ")
                if retry=='Y':
                    break
                elif retry=='N':
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

    