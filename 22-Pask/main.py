from tkinter import *

def button_encode():
    return()

def button_clear():
    check_state_1.set(0)
    check_state_2.set(0)
    check_state_3.set(0)
    check_state_4.set(0)
    check_state_5.set(0)
    entry_1.delete(0, END)
    entry_2.delete(0, END)

def checkbox_used():
    print(check_state_1.get())

def checkbox_used_2():
    print(check_state_2.get())

def checkbox_used_3():
    print(check_state_1.get())

def checkbox_used_4():
    print(check_state_2.get())

def checkbox_used_5():
    print(check_state_1.get())

def checkbox_used_6():
    print(check_state_1.get())

root = Tk()
root.title("Password generator")
root.geometry("670x200")
root.resizable(width=False, height=False)

# Labels development

label_1 = Label(text="Password     :", font=("Arial", 10))
label_2 = Label(text="Restrictions :", font=("Arial", 10))
label_3 = Label(text="Requirements :", font=("Arial", 10))
label_4 = Label(text="Master key :", font=("Arial", 10))
label_none_1 = Label(text=" ")
label_none_2 = Label(text=" ")

# Entries development

entry_1 = Entry(width=26)
entry_2 = Entry(width=26)

# Buttons development

button_1 = Button(text="Encode", command=button_encode)
button_2 = Button(text="Clear", command=button_clear)
button_3 = Button(text="Decode", command=button_clear)

# Checkboxes development

check_state_1 = IntVar()
check_state_2 = IntVar()
check_state_3 = IntVar()
check_state_4 = IntVar()
check_state_5 = IntVar()
check_state_6 = IntVar()

check_button_1 = Checkbutton(text="Digits only", variable=check_state_1, command=checkbox_used)
check_button_2 = Checkbutton(text="No special characters", variable=check_state_2, command=checkbox_used_2)
check_button_3 = Checkbutton(text="Digit", variable=check_state_3, command=checkbox_used_3)
check_button_4 = Checkbutton(text="Punctuation", variable=check_state_4, command=checkbox_used_4)
check_button_5 = Checkbutton(text="Mixed Case", variable=check_state_5, command=checkbox_used_5)
check_button_6 = Checkbutton(text="No restrictions", variable=check_state_6, command=checkbox_used_6)

# Adding password and Master key entries

label_1.grid(row=0, column=0, sticky=W)
entry_1.grid(row=0, column=1, sticky=W)
label_4.grid(row=0, column=2, sticky=W)
entry_2.grid(row=0, column=3, sticky=W)
label_none_1.grid(row=1, column=0)

# Adding restrictions

label_2.grid(row=2, column=0, sticky=W)
check_button_1.grid(row=2,column=1, sticky=W)
check_button_2.grid(row=2,column=2, sticky=W)
check_button_6.grid(row=2, column=3, sticky=W)

# Adding requirements

label_3.grid(row=3, column=0, sticky=W)
check_button_3.grid(row=3, column=1, sticky=W)
check_button_4.grid(row=3, column=2, sticky=W)
check_button_5.grid(row=3, column=3, sticky=W)
label_none_2.grid(row=4, column=0)

# Adding Buttons
button_2.grid(row=5, column=0)
button_1.grid(row=5, column=1)
button_3.grid(row=5, column=2)

root.mainloop()