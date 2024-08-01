from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
position = -100
all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if __name__ == "__main__":

    for turtle in range(6):
        turtle_name = Turtle(shape='turtle')
        turtle_name.penup()
        turtle_name.color(colors[turtle])
        turtle_name.goto(-230, position)
        position += 30
        all_turtles.append(turtle_name)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            random_move = randint(0, 10)
            turtle.forward(random_move)

            if turtle.xcor() > 230:
                is_race_on = False
                if user_bet == turtle.pencolor():
                    print(f"You win. The winner is {turtle.pencolor()}.")
                else:
                    print(f"You lost. The winner is {turtle.pencolor()}.")

screen.exitonclick()
