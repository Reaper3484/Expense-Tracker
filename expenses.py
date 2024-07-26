import json
from datetime import datetime

def expenses(current_user,spend,category):
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    for i in user["users"]:
        if current_user == i["username"]:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")      
            details = {"amount":spend,"date":date,"time":time,"category":category}
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


def money_spent(current_user, spend,category):
    
    expenses(current_user, spend,category)
    
    
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    
    
    for i in user["users"]:
        if current_user == i["username"]:
            
            latest_expense_sum = sum(item["amount"] for item in i["details"])
            i["money_spent"] = latest_expense_sum
    
    with open('user_profile.json', 'w') as Data:
        json.dump(user, Data, indent=4)
        
def filtering(current_user):
    with open('user_profile.json', 'r') as Data:
        user = json.load(Data)
    print("Filter by : ")
    print("1. Month")
    print("2. Year")
    print("3. Category")
    
    choice = int(input("Choose Filtering by Serial Number : "))
    if choice==1:
        month = int(input("Enter Month Number : "))
        year = int(input("Enter Year Number : "))
        
        for i in user["users"]:
            if current_user==i["username"]:
                for j in i["details"]:
                    if j["date"].month == month and i["details"]["date"].year == year:
                        print(i["details"])
                 