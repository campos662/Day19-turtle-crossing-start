import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
cars = []
level_up = 1

screen = Screen()
screen.title("Run tortuga, run!")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.score_refresh(nivel=level_up)
    car_manager.create_cars()
    car_manager.move_forward(mundo=level_up)
    if player.ycor() > 290:
        level_up += 1
        player.goto(0, -280)
    for car in car_manager.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
