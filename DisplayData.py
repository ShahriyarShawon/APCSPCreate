import json
import os
from Accounts import Accounts

class DataDisplayer:
    def __init__(self):
        self.account_mgr = Accounts()
    def user_prompts(self):
        print("Would you like to:")
        print("[1] Create an entry ")
        print("[2] Delete an Entry ")
        print("[3] Get password for an entry ")

    # TODO: complete the different actions 
        
        create_delete_get = int(input("Enter 1,2,3\n>  "))
        
        if create_delete_get == 1:
            
            pass        


    def display_entries(self):
        os.system('cls' if os.name == "nt" else "clear")
        print("------Here are your saved entries------")        
        with open("database.json", "r+") as f:
            content = json.load(f)
            for thing in content:
                print("*****************************************")
                print("Entry ID: " + thing)
                print("--------------------")
                print("Site: " + content[thing]["site"])
                print("Username: " + content[thing]["username"])
                print("Password: " + content[thing]["password"])
                # print("*****************************************")
        user_prompts()
                
            

# display_entries()
