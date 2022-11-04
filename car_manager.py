from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#mundo = 0
cars = []


class CarManager():
    def __init__(self):
        self.all_cars = []



    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6 :
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.left(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-240, 260))
            self.all_cars.append(new_car)




    def move_forward(self, mundo):
        DELTA = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (mundo-1))
        for car in self.all_cars:
            car.forward(DELTA)


