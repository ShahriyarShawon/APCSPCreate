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
    create_username= Entry(root, textvariable=holder)
    create_username.insert(0,'New Username')
    create_username.grid(row=1, column=1)
    create_username.bind('<Button-1>', lambda event: create_username.delete(0, END))
    
    
    passholder= StringVar()
    create_password= Entry(root, textvariable=passholder, show='*')
    create_password.grid(row=2, column=1)
    
    create_account= Button(root, text= "Create Account").grid(row=4, column=1)
    
    
    
    root.mainloop()
    

    
main()