from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Score


def screen_prepare():
    sc = Screen()
    sc.bgcolor("black")
    sc.setup(width=600, height=600)
    sc.title("My Snake Game")
    sc.tracer(0)
    return sc


if __name__ == "__main__":
    game_on = True
    screen = screen_prepare()
    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_on:
        screen.update()
        sleep(0.1)

        snake.move()
        # Detect collision with food.
        if snake.head.distance(food) < 15:
            snake.extend()
            food.food_refresh()
            score.rise_points()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset_score()
            snake.reset_snake()

        # Detect collision with tail
        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10:
                score.reset_score()
                snake.reset_snake()

    screen.exitonclick()

