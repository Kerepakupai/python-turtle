from turtle import Turtle, Screen
import random


s = Screen()
s.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start_positions = [-100, -60, -20, 20, 60, 100]
turtles = []
is_race_on = False

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.pu()
    t.goto(x=-230, y=y_start_positions[i])
    turtles.append(t)

user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        # rand_turtle = random.choice(turtles)
        turtle.fd(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()


if winner == user_bet:
    print(f"You've won. The {winner} turtle won")
else:
    print(f"You've Lost. The {winner} turtle won")

s.exitonclick()
