import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player=Player()
screen = Screen()
car=CarManager()
score=Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

screen.onkey(player.go_up,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.mov_car()

    for car_1 in car.c_car:
        if car_1.distance(player)<20:
            game_is_on=False
            score.game_over()

    if player.is_at_finish_line():
        player.get_finish_line()
        car.level_up()
        score.increase_level()


