# import colorgram
# colors = colorgram.extract('hirst.jpg', 20)
# rgb_colors = [(c.rgb[0],c.rgb[1],c.rgb[2]) for c in colors]
from turtle import Turtle, Screen
import random as rnd

color_list = [(232, 235, 240), (230, 228, 225), (232, 217, 221), 
            (245, 159, 35), (13, 95, 184), (226, 234, 230), 
            (209, 75, 98), (46, 128, 56), (158, 6, 57), 
            (252, 223, 0), (232, 169, 8), (224, 115, 165), 
            (244, 218, 47), (14, 59, 143), (96, 203, 187), 
            (10, 15, 81), (242, 154, 174), (75, 37, 8), 
            (14, 180, 9), (2, 115, 46)]

t = Turtle()
s = Screen()
s.colormode(255)
t.pu()
t.ht()
t.speed("fastest")


def set_positions(line):
    y = -250 + (line * 50)
    t.goto(-250, y)

for i in range(10):
    set_positions(i)
    for _ in range(10):
        t.dot(20, rnd.choice(color_list))
        t.fd(50)


s.exitonclick()