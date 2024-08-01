from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.f_score = 0
        self.s_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.f_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.s_score, align="center", font=("Courier", 80, "normal"))

    def f_point(self):
        self.f_score += 1
        self.update_score()

    def s_point(self):
        self.s_score += 1
        self.update_score()
