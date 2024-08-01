import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def screen_prepare():
    sc = Screen()
    sc.setup(width=600, height=600)
    sc.title("Cross the road")
    sc.tracer(0)
    return sc


def main_loop():

    game_is_on = True

    while game_is_on:
        if CarManager.car_collision(player.player_character):
            game_is_on = False
            screen.clear()
            score_obj.game_over_screen(score_obj.score)
        else:

            player.pass_level_check(score_obj)
            CarManager.car_traffic_logic(score_obj.score)

            # the screen is refreshing every 0.1 seconds to make animation smooth
            time.sleep(0.1)
            screen.update()


if __name__ == "__main__":

    screen = screen_prepare()
    player = Player()

    score_obj = Scoreboard()
    player.move_turtle(screen)
    main_loop()
    screen.exitonclick()
