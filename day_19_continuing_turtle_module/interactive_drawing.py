from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed('fastest')


def mv_forward():
    tim.forward(10)


def mv_backwards():
    tim.backward(10)


def clockwise():
    tim.setheading(tim.heading()+10)


def cntr_clockwise():
    tim.setheading(tim.heading()-10)


def clear_drawing():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(mv_forward, 'w')
screen.onkey(mv_backwards, 's')
screen.onkey(clockwise, 'd')
screen.onkey(cntr_clockwise, 'a')
screen.onkey(clear_drawing, 'c')

screen.exitonclick()
