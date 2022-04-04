import turtle
import gv
import game
import keyboard
# import wrong_input

def meniu_select():
    main_meniu_select = turtle.Turtle()
    main_meniu_select.speed(0)
    main_meniu_select.color("blue")
    main_meniu_select.penup()
    main_meniu_select.hideturtle()

    main_meniu_select.goto(0, 260)
    main_meniu_select.write("Welcome to Ping Pong game", align="center", font=("Courier", 24, "bold"))

    main_meniu_select.goto(0, 130)
    main_meniu_select.write("Please select your difficulty:", align="center", font=("Courier", 20, "bold"))

    main_meniu_select.goto(0, 100)
    main_meniu_select.write("Easy [Press E]", align="center", font=("Courier", 15, "bold"))

    main_meniu_select.goto(0, 70)
    main_meniu_select.write("Medium [Press M]", align="center", font=("Courier", 15, "bold"))

    main_meniu_select.goto(0, 40)
    main_meniu_select.write("Hard [Press H]", align="center", font=("Courier", 15, "bold"))

    main_meniu_select.goto(0, -230)
    main_meniu_select.write("| CONTROLS |", align="center",font=("Courier", 15, "bold"))

    main_meniu_select.goto(0, -260)
    main_meniu_select.write("| PLAYER 1 - W, S | PLAYER 2 - Up arrow, Down arrow |", align="center", font=("Courier", 15, "bold"))

def wrong_input():
    turtle.clearscreen()
    game.sc.bgcolor("AliceBlue")

    wrong_input = turtle.Turtle()
    wrong_input.speed(0)
    wrong_input.color("blue")
    wrong_input.penup()
    wrong_input.hideturtle()

    wrong_input.goto(0, 260)
    wrong_input.write("Welcome to Ping Pong game", align="center", font=("Courier", 24, "bold"))

    wrong_input.goto(0, 200)
    wrong_input.write("WRONG INPUT !", align="center", font=("Courier", 24, "bold"))

    wrong_input.goto(0, 130)
    wrong_input.write("Please select your difficulty again:", align="center", font=("Courier", 20, "bold"))

    wrong_input.goto(0, 100)
    wrong_input.write("Easy [Press E]", align="center", font=("Courier", 15, "bold"))

    wrong_input.goto(0, 70)
    wrong_input.write("Medium [Press M]", align="center", font=("Courier", 15, "bold"))

    wrong_input.goto(0, 40)
    wrong_input.write("Hard [Press H]", align="center", font=("Courier", 15, "bold"))

    wrong_input.goto(0, -230)
    wrong_input.write("| CONTROLS |", align="center", font=("Courier", 15, "bold"))

    wrong_input.goto(0, -260)
    wrong_input.write("| PLAYER 1 - W, S | PLAYER 2 - Up arrow, Down arrow |", align="center", font=("Courier", 15, "bold"))

    if keyboard.read_key() == "e":
        gv.ball_speed_y = -5
        gv.ball_speed_x = 5
        turtle.clearscreen()
        game.game_starts()
    elif keyboard.read_key() == "m":
        gv.ball_speed_y = -7
        gv.ball_speed_x = 7
        turtle.clearscreen()
        game.game_starts()
    elif keyboard.read_key() == "h":
        gv.ball_speed_y = -9.5
        gv.ball_speed_x = 9.5
        turtle.clearscreen()
        game.game_starts()
    else:
        wrong_input()

def start():
    meniu_select()

    if keyboard.read_key() == "e":
        gv.ball_speed_y = -5
        gv.ball_speed_x = 5
        turtle.clearscreen()
        game.game_starts()
    elif keyboard.read_key() == "m":
        gv.ball_speed_y = -7
        gv.ball_speed_x = 7
        turtle.clearscreen()
        game.game_starts()
    elif keyboard.read_key() == "h":
        gv.ball_speed_y = -9.9
        gv.ball_speed_x = 9.9
        turtle.clearscreen()
        game.game_starts()
    else:
        wrong_input()