from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FISNISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FISNISH_LINE:
            return True
        else:
            return False
