from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player_character = Turtle('turtle')
        self.player_character.color("black")
        self.player_character.penup()
        self.player_character.setheading(90)
        self.player_character.goto(STARTING_POSITION)
        self.level = 0

    def up(self):
        self.player_character.forward(MOVE_DISTANCE)

    def move_turtle(self, screen_name):
        screen_name.listen()
        screen_name.onkey(self.up, "Up")

    def pass_level_check(self, score_object):
        """Check if the player reached the finish line. If yes score+1 and return to starting position"""
        if self.player_character.ycor() > FINISH_LINE_Y:
            score_object.level_up()
            self.player_character.goto(STARTING_POSITION)
