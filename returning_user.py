from tkinter import *
import Login
import newaccount
def run_returning_user():
    root = Tk()
    root.title("Suki and Shay's Pro Password Manager")
    root.geometry("450x100")

    login_frame = Frame(root)
    login_frame.grid(row=0, column=0)

    # username
    username_label = Label(login_frame, text="Username: ")
    username_label.grid(row=0, column=0)

    username_holder = StringVar()
    login_username = Entry(login_frame, textvariable=username_holder)
    login_username.grid(row=0, column=1)


    # password
    password_label = Label(login_frame, text="Password: ")
    password_label.grid(row=1, column=0)

    password_holder = StringVar()
    login_password = Entry(login_frame, textvariable=password_holder, show="*")
    login_password.grid(row=1, column=1)


    submit_button = Button(login_frame, text="Submit", 
                            command=lambda: Login.authenticate(username_holder, password_holder)
                            ).grid(row=2, column=0)
                            


    new_account_button = Button(login_frame, text="Create New Account", 
                            command=lambda: newaccount.main()
                            ).grid(row=2, column=1)



    root.mainloop()

# run_returning_user()