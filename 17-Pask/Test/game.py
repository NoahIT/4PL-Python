import turtle
import gv

sc = turtle.Screen()
sc.title("Ping Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

def game_starts():
    left_pad = turtle.Turtle()
    left_pad.speed(0)
    left_pad.shape("square")
    left_pad.color("black")
    left_pad.shapesize(stretch_wid=6, stretch_len=2)
    left_pad.penup()
    left_pad.goto(-400, 0)

    right_pad = turtle.Turtle()
    right_pad.speed(0)
    right_pad.shape("square")
    right_pad.color("black")
    right_pad.shapesize(stretch_wid=6, stretch_len=2)
    right_pad.penup()
    right_pad.goto(400, 0)

    ball = turtle.Turtle()
    ball.speed(gv.ball_speed)
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 5
    ball.dy = -5

    score = turtle.Turtle()
    score.speed(0)
    score.color("blue")
    score.penup()
    score.hideturtle()
    score.goto(0, 260)
    score.write("Left_player : 0    Right_player: 0",
                align="center", font=("Courier", 24, "normal"))

    def paddleaup():
        y = left_pad.ycor()
        y += 20
        left_pad.sety(y)

    def paddleadown():
        y = left_pad.ycor()
        y -= 20
        left_pad.sety(y)

    def paddlebup():
        y = right_pad.ycor()
        y += 20
        right_pad.sety(y)

    def paddlebdown():
        y = right_pad.ycor()
        y -= 20
        right_pad.sety(y)

    left_player = 0
    right_player = 0

    while True:
        sc.listen()
        sc.onkeypress(paddleaup, "w")
        sc.onkeypress(paddleadown, "s")
        sc.onkeypress(paddlebup, "Up")
        sc.onkeypress(paddlebdown, "Down")
        sc.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # borders
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1

        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1

        if ball.xcor() > 500:
            ball.goto(0, 0)
            ball.dy *= -1
            left_player += 1
            score.clear()
            score.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center",
                        font=("Courier", 24, "normal"))

        if ball.xcor() < -500:
            ball.goto(0, 0)
            ball.dy *= -1
            right_player += 1
            score.clear()
            score.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center",
                        font=("Courier", 24, "normal"))

        # collision
        if (ball.xcor() > 360 and ball.xcor() < 370) and (
                ball.ycor() < right_pad.ycor() + 40 and ball.ycor() > right_pad.ycor() - 40):
            ball.setx(360)
            ball.dx *= -1

        if (ball.xcor() < -360 and ball.xcor() > -370) and (
                ball.ycor() < left_pad.ycor() + 40 and ball.ycor() > left_pad.ycor() - 40):
            ball.setx(-360)
            ball.dx *= -1
