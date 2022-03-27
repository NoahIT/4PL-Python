import turtle
import main_meniu
import easy_game as e
import medium_game as m
import hard_game as h
import keyboard

sc = turtle.Screen()
sc.title("Ping Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

main_meniu.greeting()
main_meniu.difficulty()

if sc.onkeypress() == "1":
    e.Easy_game()
elif sc.onkeypress() == "2":


sc.listen()
sc.onkeypress(e, "e")
sc.onkeypress(m, "m")
sc.onkeypress(h, "h")

turtle.mainloop()