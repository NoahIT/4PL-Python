from tkinter import *

def button_encode(text, s):
    entry_3.delete(0, END)

    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
            entry_3.insert(0, result)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
            entry_3.insert(0, result)
    return result

def button_decode(text, dec):
    entry_4.delete(0, END)

    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + dec - 65) % 26 + 65)
            res_i = int(len(entry_1.get()))
            result[:res_i]
            entry_4.insert(0, result)
        else:
            result += chr((ord(char) + dec - 97) % 26 + 97)
            res_i = int(len(entry_1.get()))
            result[:res_i]
            entry_4.insert(0, result)
    return result

#Check box functions
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
root.geometry("700x210")
root.resizable(width=False, height=False)

# Labels development
label_1 = Label(text="Password     :", font=("Arial", 10))
label_2 = Label(text="Restrictions :", font=("Arial", 10))
label_3 = Label(text="Requirements :", font=("Arial", 10))
label_4 = Label(text="Decode :", font=("Arial", 10))
label_5 = Label(text="Decoded password :", font=("Arial", 10))
label_6 = Label(text="Encoded password :", font=("Arial", 10))
label_7 = Label(text="Keyword :", font=("Arial", 10))
label_none_1 = Label(text=" ")
label_none_2 = Label(text=" ")
label_none_3 = Label(text=" ")

# Entries development
entry_1 = Entry(width=26)
entry_2 = Entry(width=26)
entry_3 = Entry(width=26)
entry_4 = Entry(width=26)

# text = entry_1.get()
# dec = entry_3.get()
# s=26

# Buttons development
button_1 = Button(text="Encode", command=lambda: button_encode(text=entry_1.get(),s=10))
button_3 = Button(text="Decode", command=lambda: button_decode(text=entry_1.get(),dec=26))

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
label_7.grid(row=0, column=2, sticky=W)
entry_2.grid(row=0, column=3, sticky=W)
label_4.grid(row=0, column=2, sticky=W)
label_none_1.grid(row=1, column=0)
label_none_3.grid(row=6, column=0)

label_6.grid(row=7, column=0, sticky=W)
entry_3.grid(row=7, column=1, sticky=W)
label_5.grid(row=7, column=2, sticky=W)
entry_4.grid(row=7, column=3, sticky=W)

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
button_1.grid(row=5, column=1)
button_3.grid(row=5, column=2)

root.mainloop()