from tkinter import *

# TODO: make id, site, and note available on the canvas

def display_and_enter():
    
    root = Tk()
    root.geometry("500x500")
    root.title("Issan app")

    view_frame = Frame(root).pack()
    entry_frame = Frame(root).pack()

    

    root.mainloop()
    

display_and_enter()
