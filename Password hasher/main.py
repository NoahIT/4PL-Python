from tkinter import *

study:

https://www.jetbrains.com/help/pycharm/navigating-through-the-source-code.html
https://www.google.com/search?q=how+to+go+deeper+inside+methods+to+see+algorithms+in+pycharm&ei=IVxxYv3FJqyOrwSO9J64CQ&ved=0ahUKEwi92sDg48P3AhUsx4sKHQ66B5cQ4dUDCA4&uact=5&oq=how+to+go+deeper+inside+methods+to+see+algorithms+in+pycharm&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BAghEApKBAhBGABKBAhGGABQjwhY1x5g0R9oAXABeACAAWeIAdkLkgEEMTcuMZgBAKABAcgBCMABAQ&sclient=gws-wiz



def generateKey(p_string, key):
    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)

    key = list(key)
    if len(p_string) == len(key):
        return(key)
    else:
        for i in range(len(p_string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cipherText(): #p_string, key):
    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)

    cipher_text = []
    for i in range(len(p_string)):
        x = (ord(p_string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))


def originalText(): #cipher_text, key):
    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))


    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)

# #Check box functions
# def checkbox_used():
#     print(check_state_1.get())
#
# def checkbox_used_2():
#     print(check_state_2.get())
#
# def checkbox_used_3():
#     print(check_state_1.get())
#
# def checkbox_used_4():
#     print(check_state_2.get())
#
# def checkbox_used_5():
#     print(check_state_1.get())
#
# def checkbox_used_6():
#     print(check_state_1.get())

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

# Buttons development
button_1 = Button(text="Encode", command=cipherText)
button_3 = Button(text="Decode", command=originalText)

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