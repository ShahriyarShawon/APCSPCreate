#Author Shahriyar

from tkinter import *
import Login
import json
from returning_user import run_returning_user
import newaccount

with open("authenticate.json", "r") as f:
    authenticate = json.load(f)
    if authenticate["first_time"] == True:
        print("This ran")   
        newaccount.main()     
    else:
        print("This ran ")
        run_returning_user()

        