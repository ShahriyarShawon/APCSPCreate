import json
from tkinter import *
# with open("authenticate.json","r") as f:
#     j_content = json.load(f)
#     print(j_content["username"])


# #changing json
# with open("authenticate.json","r+") as f:
#     content = json.load(f)
#     content["first_time"] = "true"
#     f.seek(0)
#     json.dump(content, f, indent=4)
#     f.truncate()

# from Tkinter import *

# master = Tk()

# scrollbar = Scrollbar(master)
# scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(master, yscrollcommand=scrollbar.set)
# for i in range(1000):
#     listbox.insert(END, str(i))
# listbox.pack(side=LEFT, fill=BOTH)

# scrollbar.config(command=listbox.yview)

# mainloop()

root=Tk()
frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
frame2 = Frame(root)
frame2.grid(row=0,column=1)
new = Button(frame2, text="New Account",
                 command=lambda: create_window(root)).grid(row=0, column=1)
login_button = Button(frame2, text="I already have an account, let me log in",
                        command=lambda: (
                            root.destroy(),
                            returning_user.run_returning_user()
                        )).grid(row=5, column=1)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.create_text( "40","20", text="fffffreee")
canvas.pack(side=LEFT,expand=True,fill=BOTH)
root.mainloop()