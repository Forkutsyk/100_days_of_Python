from turtle import Turtle, Screen, colormode
from random import randint

t = Turtle()
screen = Screen()
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


angle = 0
t.speed('fastest')
while angle != 360:
    t.color(random_color())
    t.circle(100)
    angle += 5
    t.setheading(angle)


screen.exitonclick()
