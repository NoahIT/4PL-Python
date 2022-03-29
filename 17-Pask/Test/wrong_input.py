import turtle
import gv
import game
import keyboard

def wrong_input():
    turtle.clearscreen()

    greeting = turtle.Turtle()
    greeting.speed(0)
    greeting.color("blue")
    greeting.penup()
    greeting.hideturtle()
    greeting.goto(0, 260)
    greeting.write("WRONG INPUT !", align="center", font=("Courier", 24, "bold"))

    difficulty_s = turtle.Turtle()
    difficulty_s.speed(0)
    difficulty_s.color("blue")
    difficulty_s.penup()
    difficulty_s.hideturtle()
    difficulty_s.goto(0, 130)
    difficulty_s.write("Please select your difficulty again:", align="center", font=("Courier", 20, "bold"))

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

    game.sc.listen()
    if keyboard.read_key() == "e":
        gv.ball_speed = 40
        turtle.clearscreen()
        game.game_starts()
    elif keyboard.read_key() == "m":
        gv.ball_speed = 65
        turtle.clearscreen()
        game.game_starts()
    elif keyboard.read_key() == "h":
        gv.ball_speed = 100
        turtle.clearscreen()
        game.game_starts()
    else:
        wrong_input()