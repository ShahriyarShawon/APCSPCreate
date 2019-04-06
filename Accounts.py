import json

from CryptoTools import CryptoTools
import DisplayData.DataDisplayer


class Accounts:
    def __init__(self):
        self.crypt = CryptoTools()
        self.data_displayer = DataDisplayer() 
        # print(self.crypt)
        
    def create_account(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        password = self.crypt.encrypt(password)
        
        with open("account.json","r+") as f:
            content = json.load(f)
            content["username"] = username
            content["password"] = password
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate()

    def sign_in(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        password = self.crypt.encrypt(password)

        with open("account.json","r") as f:
            content = json.load(f)
        if content["username"] == username and content["password"] == password:
            self.data_displayer.display_entries()
        else:
            print("Sorry, either your username or pasword was not matched in the login ")
            # print("")
            fail_input = input("Press 1 to try again or 2 to create a new account")
            
    def create_entry(self,site,username,enc_password):
        with open("database.json","r+") as f:
            content = json.load(f)
            content[self.crypt.gen_rand_id(8)] = {"site":site,
                                            "username":username,
                                            "password":enc_password,
                                            }
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate()            
        
            
    def delete_login(self,entry_id):
        with open("database.json","r+") as f:
            content = json.load(f)
            del content[entry_id]
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate()            
        pass

# account = Accounts()
# # account.create_entry("asite.com","ausername","apassword")
# account.create_account()