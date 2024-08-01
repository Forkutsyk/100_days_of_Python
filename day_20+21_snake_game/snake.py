from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
WALKING_PACE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.creating_starting_body()
        self.head = self.snake_body[0]

    def creating_starting_body(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(position)
        self.snake_body.append(new_seg)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def reset_snake(self):
        for segment in self.snake_body:
            segment.hideturtle()
        self.snake_body.clear()
        self.creating_starting_body()
        self.head = self.snake_body[0]

    def move(self):
        for position in range(len(self.snake_body) - 1, 0, -1):
            new_y = self.snake_body[position - 1].ycor()
            new_x = self.snake_body[position - 1].xcor()
            self.snake_body[position].goto(new_x, new_y)
        self.head.forward(WALKING_PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)



