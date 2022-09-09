from turtle import Turtle, Screen
from random import randint


def draw_shape(sides: int) -> None:
    for _ in range(sides):
        angle = 360 / sides
        turtle.right(angle)
        turtle.forward(100)


if __name__ == "__main__":
    turtle = Turtle()
    screen = Screen()
    screen.colormode(255)

    for n_sides in range(3, 11):
        turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        draw_shape(n_sides)

    screen.exitonclick()
