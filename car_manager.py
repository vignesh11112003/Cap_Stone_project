
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle
class CarManager:
    def __init__(self):
        self.c_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            r_y = random.randint(-250, 250)
            new_car.goto(300, r_y)
            self.c_car.append(new_car)

    def mov_car(self):
        for c in self.c_car:
            c.backward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT

