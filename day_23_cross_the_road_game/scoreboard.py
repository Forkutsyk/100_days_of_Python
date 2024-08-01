from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_score()

    def game_over_screen(self, score):
        self.goto(0, 0)
        self.write(f"GAME OVER. Your score is: {score}", align="center", font=("Arial", 24, "normal"))
