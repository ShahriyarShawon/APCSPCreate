import json

def get_info(username_holder, password_holder):
    j_username = ""
    j_password = ""
    username = username_holder.get()
    password = password_holder.get()
    
    with open("authenticate.json","r") as f:
        j_content = json.load(f)
        j_username = j_content["username"]
        j_password = j_content["password"]
    return password
def authenticate(username_holder, password_holder):
    get_info(username_holder, password_holder)
    