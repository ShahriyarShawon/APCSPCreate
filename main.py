from tkinter import *
import Login
import json
from returning_user import run_returning_user

with open("authenticate.json", "r") as f:
    authenticate = json.load(f)
    if authenticate["first_time"] == True:
        print("This ran")        
    else:
        run_returning_user()

        