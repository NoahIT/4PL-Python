from tkinter import *

def listbox_used(event):
    if list_box.get(list_box.curselection()) is not None:
        entry_1.delete(0,"end")
        entry_1.insert(END, list_box.get(list_box.curselection()))

window = Tk()
window.title("Registration form")
window.minsize(width=300, height=200)

label = Label(text="Registration:", font=("Arial", 14, "bold"))
label.pack()

entry_1 = Entry(width=200)
entry_1.insert(END, string="Username")
entry_2 = Entry(width=200)
entry_2.insert(END, string="Password")
entry_3 = Entry(width=200)
entry_3.insert(END, string="Repeat Password")

entry_1.pack()
entry_2.pack()
entry_3.pack()
#
# list_box = Listbox(height=4)
# for item in global_variables.usernames:
#     list_box.insert(global_variables.usernames.index(item), item)
#
# list_box.bind("<<ListboxSelect>>", listbox_used)
# list_box.pack(fill=X)
#
# button = Button(text="Log In", command=log_in)
# button.pack(fill=X)
# button = Button(text="Sign In", command=sign_in)
# button.pack(fill=X)
#

window.mainloop()