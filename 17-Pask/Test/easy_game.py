import turtle

class Easy_game():
    sc2 = turtle.Screen()
    sc2.title("Ping Pong game")
    sc2.bgcolor("white")
    sc2.setup(width=1000, height=600)

    left_pad = turtle.Turtle()
    left_pad.speed(0)
    left_pad.shape("square")
    left_pad.color("black")
    left_pad.shapesize(stretch_wid=4, stretch_len=1)
    left_pad.penup()
    left_pad.goto(-400, 0)

    right_pad = turtle.Turtle()
    right_pad.speed(0)
    right_pad.shape("square")
    right_pad.color("black")
    right_pad.shapesize(stretch_wid=4, stretch_len=1)
    right_pad.penup()
    right_pad.goto(400, 0)

    ball = turtle.Turtle()
    ball.speed(40)
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 5
    ball.dy = -5

    left_player = 0
    right_player = 0

    score = turtle.Turtle()
    score.speed(0)
    score.color("blue")
    score.penup()
    score.hideturtle()
    score.goto(0, 260)
    score.write("Left_player : 0    Right_player: 0",
                align="center", font=("Courier", 24, "normal"))

    def paddleaup(self):
        y = Easy_game.left_pad.ycor()
        y += 20
        Easy_game.left_pad.sety(y)

    def paddleadown(self):
        y = Easy_game.left_pad.ycor()
        y -= 20
        Easy_game.left_pad.sety(y)

    def paddlebup(self):
        y = Easy_game.right_pad.ycor()
        y += 20
        Easy_game.right_pad.sety(y)

    def paddlebdown(self):
        y = Easy_game.right_pad.ycor()
        y -= 20
        Easy_game.right_pad.sety(y)

        Easy_game.sc2.listen()
        Easy_game.sc2.onkeypress(Easy_game.paddleaup, "w")
        Easy_game.sc2.onkeypress(Easy_game.paddleadown, "s")
        Easy_game.sc2.onkeypress(Easy_game.paddlebup, "Up")
        Easy_game.sc2.onkeypress(Easy_game.paddlebdown, "Down")

while True:
    Easy_game.sc2.update()

    Easy_game.ball.setx(Easy_game.ball.xcor() + Easy_game.ball.dx)
    Easy_game.ball.sety(Easy_game.ball.ycor() + Easy_game.ball.dy)

    # Checking borders
    if Easy_game.ball.ycor() > 280:
        Easy_game.ball.sety(280)
        Easy_game.ball.dy *= -1

    if Easy_game.ball.ycor() < -280:
        Easy_game.ball.sety(-280)
        Easy_game.ball.dy *= -1

    if Easy_game.ball.xcor() > 500:
        Easy_game.ball.goto(0, 0)
        Easy_game.ball.dy *= -1
        Easy_game.left_player += 1
        Easy_game.score.clear()
        Easy_game.score.write("Left_player : {}    Right_player: {}".format(Easy_game.left_player, Easy_game.right_player), align="center",
                        font=("Courier", 24, "normal"))

    if Easy_game.ball.xcor() < -500:
        Easy_game.ball.goto(0, 0)
        Easy_game.ball.dy *= -1
        Easy_game.right_player += 1
        Easy_game.score.clear()
        Easy_game.score.write("Left_player : {}    Right_player: {}".format(Easy_game.left_player, Easy_game.right_player), align="center",
                        font=("Courier", 24, "normal"))

        # Paddle ball collision
    if (Easy_game.ball.xcor() > 360 and Easy_game.ball.xcor() < 370) and (
        Easy_game.ball.ycor() < Easy_game.right_pad.ycor() + 40 and Easy_game.ball.ycor() > Easy_game.right_pad.ycor() - 40):
        Easy_game.ball.setx(360)
        Easy_game.ball.dx *= -1

    if (Easy_game.ball.xcor() < -360 and Easy_game.ball.xcor() > -370) and (
        Easy_game.ball.ycor() < Easy_game.left_pad.ycor() + 40 and Easy_game.ball.ycor() > Easy_game.left_pad.ycor() - 40):
        Easy_game.ball.setx(-360)
        Easy_game.ball.dx *= -1
