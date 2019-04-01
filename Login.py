import json
from Encryptor import Encryptor

def get_info(username_holder, password_holder):
    j_username = ""
    j_password = ""
    username = username_holder.get()
    password = password_holder.get()
    
    with open("authenticate.json","r") as f:
        j_content = json.load(f)
        j_username = j_content["username"]
        j_password = j_content["password"]
    
    return j_username, j_password, username, password

def authenticate(username_holder, password_holder):
    j_username, j_password, username, password = get_info(username_holder, password_holder)
    encryptor = Encryptor()
    enc_user_pass = encryptor.encrypt(password)
    if enc_user_pass == j_password and j_username == username:
        print("Login successful!")
    else:
        print("The username or password does not match what we have in the database")
       



    