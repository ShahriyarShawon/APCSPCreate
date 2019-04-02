#author suki
from Tkinter import *

def main():
    root = Tk()
    root.geometry("450x100")
    new=Button(root, text ="New Account", command= create_window).pack()
    root.mainloop()
def create_window():
    root = Tk()
    root.geometry("450x100")
    holder= StringVar()
    create_username= Entry(root, textvariable=holder, show="*")
    create_username.grid(row=1, column=1)
    
    create_password
    root.mainloop()
    
    
main()