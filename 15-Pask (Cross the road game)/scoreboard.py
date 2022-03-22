from turtle import Turtle

FONT = ("Roboto", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f"level {self.level}", align= "left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=FONT)