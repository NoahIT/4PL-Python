import venv
from tkinter import *
from tkinter import messagebox

def clear_entry1(event):
   entry_1.delete(0, END)

def clear_entry2(event):
   entry_2.delete(0, END)

def clear_entry3(event):
   entry_3.delete(0, END)

def button_clicked():
    if len(entry_1.get()) or len(entry_2.get()) or len(entry_3.get()) == 0:
        messagebox.showinfo("Information", "tu smirdi")
    if len(entry_1.get()) == 0:
        messagebox.showinfo("Information", "Username entry is not filled\nEnter your selected username")
    elif len(entry_2.get()) == 0:
        messagebox.showinfo("Information", "Password entry is not filled\nEnter your selected password")
    elif len(entry_3.get()) == 0:
        messagebox.showinfo("Information", "Repeat password entry is not fille\nRepeat your password")
    else:
        pass

def button_clicked_2():
    exit()

window = Tk()
window.title("Registration form")
window.minsize(width=300, height=200)

label = Label(text="--------------   Registration   --------------", font=("Arial", 14, "bold"))
label_2 = Label(text="Enter your username here:", font=("Arial", 10))
label_3 = Label(text="Enter your password here:", font=("Arial", 10))
label_4 = Label(text="Repeat your password here:", font=("Arial", 10))

entry_1 = Entry(width=50)
entry_1.insert(0, string="Username")
entry_1.bind("<Button-1>", clear_entry1)

entry_2 = Entry(width=50)
entry_2.insert(END, string="Password")
entry_2.bind("<Button-1>", clear_entry2)

entry_3 = Entry(width=50)
entry_3.bind("<Button-1>", clear_entry3)

button = Button(text="Sign In", command=button_clicked)
button_2 = Button(text="Exit", command=button_clicked_2)

entry_3.insert(END, string="Repeat Password")
label.pack()
label_2.pack()
entry_1.pack(expand=YES)
label_3.pack()
entry_2.pack(expand=YES)
label_4.pack()
entry_3.pack(expand=YES)
button.pack(fill=X)
button_2.pack(fill=X)

window.mainloop()