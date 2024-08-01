from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

MAX_AMOUNT_CARS = 30


class CarManager(Turtle):
    car_array = []
    creation_delay = 10
    speed = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.set_random_location()
        self.shapesize(stretch_wid=1, stretch_len=2)

    def set_random_location(self):
        random_y = random.randint(-225, 275)
        random_x = random.randint(325, 450)
        self.goto(random_x, random_y)

    @classmethod
    def define_speed(cls, level):
        """Player starts with the base speed 5, and while he level upping the speed is incrementing by 10"""
        cls.speed = STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT)
        # print(f"speed: {cls.speed}")

    @classmethod
    def traffic_cleaning(cls):
        """ Deleting the car if went out the screen scope (-350 on x cord)"""
        for car in cls.car_array:
            car.forward(cls.speed)

            if car.xcor() < -350:
                car.hideturtle()
                cls.car_array.remove(car)
        # print(len(cls.car_array))

    @classmethod
    def traffic_creation(cls):
        """Creating small traffic, something between 1-3 cars"""
        number_of_cars = random.randint(1, 3)
        for _ in range(number_of_cars):
            new_car = cls()
            cls.car_array.append(new_car)

    @classmethod
    def car_traffic_logic(cls, score):
        """Create small traffic(something between 1-3 cars) every 10 milliseconds.
         Keep the amount of cars on screen >= 30"""
        car_array_len = len(cls.car_array)
        cls.define_speed(score)

        CarManager.traffic_cleaning()

        if cls.creation_delay == 10 and car_array_len < MAX_AMOUNT_CARS:
            CarManager.traffic_creation()
            cls.creation_delay = 0

        elif car_array_len >= MAX_AMOUNT_CARS:
            cls.creation_delay = 0

        cls.creation_delay += 1
        # print(f"CD: {cls.creation_delay}")

    @classmethod
    def car_collision(cls, player):
        """Check if any car collides with the player. Return True or False"""
        for car in cls.car_array:
            if car.distance(player) < 20:
                return True
        return False
