import json


class User: 
    def __init__(self,name,username,pwd):
        self.name = name
        self.username = username
        self.pwd = pwd
        
        self.expenses=[]
        self.budget=0
        
    def change_pass(self):
        old = input("Enter Old Password : ")
        if old==self.pwd:
            new_pwd = input("Enter New Password : ")
            self.pwd = new_pwd


    
