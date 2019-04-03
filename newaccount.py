# author suki
from tkinter import *
import returning_user


def main():
    root = Tk()
    root.geometry("225x100")
    new = Button(root, text="New Account",
                 command=lambda: create_window(root)).grid(row=0, column=1)
    login_button = Button(root, text="I already have an account, let me log in",
                          command=lambda: (
                              root.destroy(),
                              returning_user.run_returning_user()
                          )).grid(row=5, column=1)
    root.mainloop()


def create_window(prev_window):
    prev_window.destroy()
    root = Tk()
    root.geometry("450x100")

    username_label = Label(root, text="Username: ").grid(row=0, column=0)
    password_label = Label(root, text="Password: ").grid(row=1, column=0)

    username_holder = StringVar()
    create_username = Entry(root, textvariable=username_holder)
    create_username.insert(0, 'New Username')
    create_username.grid(row=0, column=1)
    create_username.bind(
        '<Button-1>', lambda event: create_username.delete(0, END))

    passholder = StringVar()
    create_password = Entry(root, textvariable=passholder, show='*')
    create_password.grid(row=1, column=1)

    create_account = Button(root, text="Create Account").grid(row=4, column=1)

    root.mainloop()
