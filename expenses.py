import json
from datetime import datetime

def expenses(current_user,spend):
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    for i in user["users"]:
        if current_user == i["username"]:
            now = datetime.now()
            formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
            new_expense={formatted_datetime:spend}
            i["expenses"].append(new_expense)
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


def money_spent(current_user,spend):
    expenses(current_user,spend)
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    for i in user["users"]:
        latest_expense_sum=0
        if current_user == i["username"]:
            for j in i["expenses"]:
                latest_expense_sum+=sum(j.values())
            i["money_spent"]=latest_expense_sum
    with open('user_profile.json', 'w') as Data:
        json.dump(user, Data, indent=4)
    
    