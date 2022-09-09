from turtle import Turtle, Screen
import random as rnd

direction = [0, 90, 180, 270]

turtle = Turtle()
turtle.pensize(10)
turtle.speed("fast")

screen = Screen()
screen.colormode(255)

for _ in range(100):
    turtle.pencolor(rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
    turtle.setheading(rnd.choice(direction))
    turtle.forward(40)


screen.exitonclick()