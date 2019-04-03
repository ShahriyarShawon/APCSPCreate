#Author Shahriyar

from tkinter import *
import Login
import json
from returning_user import run_returning_user
import newaccount

with open("authenticate.json", "r") as f:
    authenticate = json.load(f)
    if authenticate["first_time"] == True:        
        newaccount.main()     
    else:
        run_returning_user()

        