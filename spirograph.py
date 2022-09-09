from random import randint
from turtle import Turtle, Screen


t = Turtle()
t.speed("fastest")
s = Screen()
s.colormode(255)

while True:
    t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    t.circle(100)
    t.seth(t.heading() + 5)
    if t.heading() == 0.0:
        break


s.exitonclick()