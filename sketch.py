from turtle import Turtle, Screen

t = Turtle()
s = Screen()

t.width(2)

def move_forwards():
    t.fd(10)

def move_backwards():
    t.bk(10)

def clear():
    t.reset()

def turn_left():
    t.seth(t.heading() + 10)

def turn_right():
    t.seth(t.heading() - 10)


s.listen()
s.onkey(fun=move_forwards, key="w")
s.onkey(fun=move_backwards, key="s")
s.onkey(fun=clear, key="c")
s.onkey(fun=turn_left, key="a")
s.onkey(fun=turn_right, key="d")

s.exitonclick()