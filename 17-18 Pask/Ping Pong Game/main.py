import turtle
import main_meniu

sc = turtle.Screen()
sc.title("Ping Pong 2. Space invaders (Exam_2)")
sc.bgcolor("AliceBlue")
sc.setup(width=1000, height=600)

main_meniu.start()

turtle.exitonclick()
turtle.mainloop()