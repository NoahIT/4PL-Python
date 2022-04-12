from tkinter import *
from tkinter import messagebox
import time

work_times = 0

def start_up():
    label = Label(text="Enter your task name below: ", font=("Arial", 14))
    name_input = Entry(width=50)

    label.pack(fill=X)
    name_input.pack(fill=X)

    text = name_input.get()
    if len(text) > 0:
        name_label = Label(text=f"Task {text} is running pomodoro technique right now", font=("Arial", 14, "bold"))
        name_label.pack()
        label.config(text="Task submitted and the timer has started")
        button_clicked()

def long_break():
    for i in range(1800):            # 30 min. = 1800 sec.-------------------------------------
        print(i ," seconds\n")
        time.sleep(1)
        if i == 1800:
            messagebox.showinfo("Information",
                                "Cycle finished:\n"
                                "Worked: 1 Hour 40 Minutes\n"
                                "Rested: 30 Minutes\n")
            button_clicked()

def short_break():
    for i in range(300):            # 5 min. = 300 sec.-------------------------------------
        print(i ," seconds\n")
        time.sleep(1)
        if i == 300:
            messagebox.showinfo("Information",
                                "Your 5 min break just ended, start your work !")
            button_clicked()

def button_clicked():

    for i in range(15):             # 25 min. = 1500 sec.-------------------------------------
        print(i ," seconds\n")
        time.sleep(1)
        if i == 15:
            messagebox.showinfo("Information",
                                "Your 5 min break is up !")
            work_times = work_times + 1
            if work_times == 4:
                long_break()
            else:
                short_break()
