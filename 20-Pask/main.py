from tkinter import *
import logic

window = Tk()
window.title("Pomodoro Technique")
window.minsize(width=400, height=200)

button = Button(text="Submit and start the pomodoro technique",  command=logic.start_up())
button.pack(fill=X)

window.mainloop()





#   sutvarkyti mygtukus (command ran while button was not pressed issue - fix)
#   liko padaryti task'u list box'a ir pomidoru nuotraukas   !!!
#   itraukti i main page su kiekvienu ciklo apsisukimu       !!!
#
#          PAVEIKSLIUKO PRIDEJIMAS
#
# canvas = Canvas(window, width = 400, height = 400)
# canvas.pack()
# img = PhotoImage(file="tomato.png")
# canvas.create_image(20,20, anchor=NW, image=img)