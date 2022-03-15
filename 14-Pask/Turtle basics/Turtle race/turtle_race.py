from turtle import *
import math
import random
import turtle

wn_length = 500
wn_height = 500
turtles = 8
turtle.screensize(wn_length, wn_height)

class racer(object):
    textbox = turtle.textinput("\nTake a bet",
                               "Enter the color of the turtle you think is going to win\n"
                               "(yellow, blue, green, cyan, red, purple, pink, brown, black)\n")

    print(textbox)

    def __init__(self, color, position):
        self.position = position
        self.color = color
        self.tur = turtle.Turtle()
        self.tur.shape('turtle')
        self.tur.color(color)
        self.tur.penup()
        self.tur.setpos(position)
        self.tur.setheading(90)

    def move1(self):
        rand = random.randrange(1, 20)
        self.position = (self.position[0], self.position[1] + rand)
        self.tur.pendown()
        self.tur.forward(rand)

    def reset1(self):
        self.tur.penup()
        self.tur.setposition(self.position)


def setupfile(name, colors):
    file1 = open(name, 'w')
    for color in colors:
        file1.write(color + ' 0 \n')
    file1.close()


def startGame1():
    turtle.bgcolor('black')
    print(racer.textbox)

    t_List = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["yellow", "blue", "green", 'cyan', 'red', 'purple', 'pink', 'brown', 'black']
    start = -(wn_length/2) + 20

    for t in range(turtles):
        newpositionX = start + t*(wn_length)//turtles
        t_List.append(racer(colors[t],(newpositionX, -230)))
        t_List[t].tur.showturtle()

    run = True
    while run:
        for t in t_List:
            t.move1()

        maxcolor = []
        maxdis = 0
        for t in t_List:
            if t.position[1] > 230 and t.position[1] > maxdis:
                maxdis = t.position[1]
                maxcolor = []
                maxcolor.append(t.color)
            elif t.position[1] > 230 and t.position[1] == maxdis:
                maxDis = t.pos[1]
                maxcolor.append(t.color)

        if len(maxcolor) > 0:
            run = False
            print('The winner is: ')
            for win in maxcolor:
                print(win)

    oldscore1 = []
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        oldscore1.append([color, score])

    file.close()

    file = open('scores.txt', 'w')

    for entry in oldscore1:
        for winner in maxcolor:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1

        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')

    if racer.textbox == win:
        print("!!! You won taking this bet !!!")
    else:
        print("!!! The other colored turtle won, try again next time. !!!")

    file.close()

# mob = True
#
# def start():
#     if mob == True:
#         start = input('Would you like to play this race (enter yes/no): ')
#         if start == 'yes':
#             startGame1()
#         elif start == 'no':
#             print('\nGoodbye !')
#             exit()
#         else:
#             print ("\nSorry, that was an invalid command!")
#             start()
#
# while True:
#     print('-----')
#     start = input('Would you like to play again')
#     startGame1()