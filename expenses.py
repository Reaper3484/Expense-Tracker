import json
from datetime import datetime

def expenses(current_user,spend):
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    for i in user["users"]:
        if current_user == i["username"]:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")
            details = {"amount":spend,"date":date,"time":time}
            i["details"].append(details)
    with open('user_profile.json', 'w') as Data:
        json.dump(user, Data, indent=4)



def allocate_budget(current_user,budget):
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    for i in user["users"]:
        if current_user == i["username"]:
            i["budget"]=budget
    with open('user_profile.json', 'w') as Data:
        json.dump(user, Data, indent=4)


def money_spent(current_user, spend):
    
    expenses(current_user, spend)
    
    
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    
    
    for i in user["users"]:
        if current_user == i["username"]:
            
            latest_expense_sum = sum(item["amount"] for item in i["details"])
            i["money_spent"] = latest_expense_sum
    
    with open('user_profile.json', 'w') as Data:
        json.dump(user, Data, indent=4)