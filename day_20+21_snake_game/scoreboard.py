from turtle import Turtle

STARTING_POINT = (0, 270)
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.points = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POINT)
        self.color("white")
        self.show_points()

    def show_points(self):
        self.clear()
        self.write(arg=f"Score: {self.points} Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def rise_points(self):
        self.points += 1
        self.show_points()

    def reset_score(self):
        if self.points > self.highest_score:
            with open("data.txt", mode='w') as file:
                self.highest_score = self.points
                file.write(f"{self.highest_score}")
        self.points = 0
        self.show_points()



def reset_score(self):
    if self.points > self.highest_score:
        with open("data.txt", mode='w') as file:
            self.highest_score = self.points
            file.write(f"{self.highest_score}")
    self.points = 0
    self.show_points()