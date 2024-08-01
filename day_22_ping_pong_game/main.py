from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score


def screen_prepare():
    sc = Screen()
    sc.bgcolor("black")
    sc.setup(width=800, height=600)
    sc.title("My Pong Game")
    sc.tracer(0)
    return sc


def make_table():
    # making the net on the centre
    for position in range(290, -310, -20):
        center = Paddle((0, position))
        center.color("white")
        center.shapesize(stretch_wid=0.5, stretch_len=0.3)

    right_wall = Paddle((380, 0))
    right_wall.color("white")
    right_wall.shapesize(stretch_wid=30, stretch_len=0.1)

    left_wall = Paddle((-380, 0))
    left_wall.color("white")
    left_wall.shapesize(stretch_wid=30, stretch_len=0.1)

    down_wall = Paddle((0, -300))
    down_wall.color("white")
    down_wall.shapesize(stretch_wid=0.1, stretch_len=38)

    up_wall = Paddle((0, 300))
    up_wall.color("white")
    up_wall.shapesize(stretch_wid=0.1, stretch_len=38)


def move_paddle():
    screen.listen()

    screen.onkey(first_paddle.up, "w")
    screen.onkey(second_paddle.up, "Up")
    screen.onkey(first_paddle.down, "s")
    screen.onkey(second_paddle.down, "Down")


def main_game_loop():
    game_is_on = True
    while game_is_on:

        # winning check
        if score.f_score == 5 or score.s_score == 5:
            screen.clear()
            screen.bgcolor("black")
            result = Ball()
            result.hideturtle()

            if score.f_score == score.s_score:
                result.write("It's a draw!\nThank you for playing!", align="center", font=("Arial", 24, "normal"))
            if score.f_score > score.s_score:
                result.write(f"{player_1} won!\nThank you for playing!", align="center", font=("Arial", 24, "normal"))
            else:
                result.write(f"{player_2} side won!\nThank you for playing!", align="center", font=("Arial", 24, "normal"))
            game_is_on = False

        sleep(ball.ball_speed)
        screen.update()
        ball.move()

        # detect collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # detect collision with the paddle
        if (ball.distance(second_paddle) < 50 and ball.xcor() > 320
                or ball.distance(first_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # detect if the ball go out of the table
        if ball.xcor() > 380:
            score.f_point()
            ball.reset_position()
        if ball.xcor() < -380:
            score.s_point()
            ball.reset_position()


if __name__ == "__main__":
    screen = screen_prepare()
    # make_table()
    player_1 = screen.textinput("Player 1", "Please enter your name")
    player_2 = screen.textinput("Player 2", "Please enter your name")
    first_paddle = Paddle((-350, 0))
    second_paddle = Paddle((350, 0))
    ball = Ball()
    score = Score()

    make_table()

    # Paddle moves
    move_paddle()

    main_game_loop()
    screen.exitonclick()
