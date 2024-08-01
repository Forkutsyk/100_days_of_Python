from turtle import Turtle, Screen, colormode
from random import choice, randint

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#          "SeaGreen"]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


t = Turtle()
colormode(255)
direction = [0, 90, 180, 270]

t.speed('fastest')
t.width(15)

for move in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(choice(direction))


screen = Screen()
screen.exitonclick()
