import json

from CryptoTools import CryptoTools


class Accounts:
    def __init__(self):
        self.CryptoTools = CryptoTools()
    def create_account(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        password = self.CryptoTools.encrypt(password)
        
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
        password = self.CryptoTools.encrypt(password)

        with open("account.json","r") as f:
            content = json.load(f)
        if content["username"] == username and content["password"] == password:
            # logged in
            pass
        # TODO: Make the sign in lead to something
        else:
            print("Sorry, either your username or pasword was not matched in the login ")
            # print("")
            fail_input = input("Press 1 to try again or 2 to create a new account")