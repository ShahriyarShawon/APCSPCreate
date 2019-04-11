import os
import json
import random
import string

class PassMger:
    def __init__(self):
        self.osCommandString = "notepad.exe database.json"
        pass
        
    def open_database(self):        
        os.system(self.osCommandString)
        print("I should have opened ")
            
    def user_prompts(self):
        print("Would you like to:")
        print("[1] Create an entry ")
        print("[2] Delete an Entry ")
        print("[3] Get password for an entry ")

    # TODO: complete the different actions 
        
        create_delete_get = int(raw_input(">  "))
        
        if create_delete_get == 1:
            self.create_entry()
        elif create_delete_get == 2:
            self.open_database()
            entry_to_delete = raw_input("Enter the Entry id of the Entry you would like to get rid of \n> ")
            self.delete_login(entry_to_delete)
        elif create_delete_get == 3:
            self.open_database()
            entry_to_get_pass = raw_input("Enter the id of the password you want to retrieve\n> ")
            self.get_pass_for_entry(entry_to_get_pass)
            
                    


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
        self.user_prompts()              
  

        
    def create_account(self):
        username = raw_input("Enter a username: ")
        password = raw_input("Enter a password: ")
        password = self.encrypt(password)
        
        with open("account.json","r+") as f:
            content = json.load(f)
            content["username"] = username
            content["password"] = password
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate()
        #TODO: inform user to now login with the same information
        self.sign_in()

    def sign_in(self):
        username =raw_input("Enter your Username: ")
        password = raw_input("Enter your Password: ")
        password = self.encrypt(password)

        with open("account.json","r") as f:
            content = json.load(f)
        if content["username"] == username and content["password"] == password:
            self.display_entries()
        else:
            print("Sorry, either your username or pasword was not matched in the login ")
            # print("")
            fail_input = int(raw_input("Press 1 to try again or 2 to create a new account"))
            if fail_input == 1:
                self.sign_in()
            elif fail_input == 2:
                self.create_account()
            else:
                self.sign_in()
            
            
    def create_entry(self):
        site = raw_input("Enter the Site of Login: ")
        username = raw_input("Enter your username for " + site + ": ")
        enc_password = self.encrypt(raw_input("Enter your password for " + site + ": "))
        with open("database.json","r+") as f:
            content = json.load(f)
            content[self.gen_rand_id(8)] = {"site":site,
                                            "username":username,
                                            "password":enc_password,
                                            }
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate()  
        self.user_prompts()
        
        
            
    def delete_login(self,entry_id):
        # self.display_entries()
        # self.open_database()
        with open("database.json","r+") as f:
            content = json.load(f)
            del content[entry_id]
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate() 
        self.user_prompts()           
        
    # TODO: make password more visible
    def get_pass_for_entry(self,entry_id):
        # self.display_entries()
        # self.open_database()
        with open("database.json", "r") as f:
            content = json.load(f)
            print(self.decrypt(content[entry_id]["password"]))
        self.user_prompts()
        
        
    def gen_rand_id(self, length):
        # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/34017605#34017605
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

    def encrypt(self, raw_password):
        enc_pass = ""
        for letter in raw_password:
            enc_pass += hex(ord(letter)).replace("0x","").replace("6","!X:2").replace("5","&^~").replace("4","[]_{+-")
        # print(enc_pass)
        return enc_pass

    def decrypt(self, enc_password):
        enc_password =  enc_password.replace("!X:2","6").replace("&^~","5").replace("[]_{+-","4")
        raw_pass = bytearray.fromhex(enc_password).decode('utf-8')
        # print(raw_pass)
        return raw_pass

