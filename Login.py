import json

def get_info():
    with open("authenticate.json","r") as f:
        authenticate = json.load(f)
        print(authenticate)
    



def authenticate_login(username, password):
    get_info()
    username = username.get()
    password = password.get()

    # print("Username is " + username + " Password is " + password)