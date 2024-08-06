from turtle import Turtle
from collections import deque
import random

COLORS = ["red", "yellow", "orange", "green", "blue", "purple"]


class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = deque()
        self.pace = 0.1

    def create_car(self):
        generate_probability = random.randint(1, 6)
        if generate_probability == 1:
            new_car = Turtle("square")
            new_car.shapesize(1.25, 2.25)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.speed(0)
            new_car.goto(300, random.randint(-210, 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(10)

    def pace_increase(self):
        self.pace -= (self.pace / 8)

    def remove(self):
        self.cars.popleft()
