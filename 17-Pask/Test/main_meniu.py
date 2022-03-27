import turtle

def greeting():
    greeting = turtle.Turtle()
    greeting.speed(0)
    greeting.color("blue")
    greeting.penup()
    greeting.hideturtle()
    greeting.goto(0, 260)
    greeting.write("Welcome to Ping Pong game", align="center", font=("Courier", 24, "bold"))

def difficulty():
    difficulty_s = turtle.Turtle()
    difficulty_s.speed(0)
    difficulty_s.color("blue")
    difficulty_s.penup()
    difficulty_s.hideturtle()
    difficulty_s.goto(0, 130)
    difficulty_s.write("Please select your difficulty:", align="center", font=("Courier", 20, "bold"))

    difficulty_se = turtle.Turtle()
    difficulty_se.speed(0)
    difficulty_se.color("blue")
    difficulty_se.penup()
    difficulty_se.hideturtle()
    difficulty_se.goto(0, 100)
    difficulty_se.write("Easy [Press E]", align="center", font=("Courier", 15, "bold"))

    difficulty_sm = turtle.Turtle()
    difficulty_sm.speed(0)
    difficulty_sm.color("blue")
    difficulty_sm.penup()
    difficulty_sm.hideturtle()
    difficulty_sm.goto(0, 70)
    difficulty_sm.write("Medium [Press M]", align="center", font=("Courier", 15, "bold"))

    difficulty_sh = turtle.Turtle()
    difficulty_sh.speed(0)
    difficulty_sh.color("blue")
    difficulty_sh.penup()
    difficulty_sh.hideturtle()
    difficulty_sh.goto(0, 40)
    difficulty_sh.write("Hard [Press H]", align="center", font=("Courier", 15, "bold"))