from turtle import Turtle, Screen
from random import choice

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

t = Turtle()
s = Screen()

sides = 3
for figure in range(7):
    for side in range(sides):
        t.forward(100)
        t.rt(360 / sides)
    t.color(choice(colours))
    sides += 1


