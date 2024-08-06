from turtle import Screen
from player import Player
from traffic import Traffic
from scoreboard import Scoreboard
import time

cars = []
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.screensize(600, 600)
screen.title("Crossy Turtle")

player = Player()
scoreboard = Scoreboard()
traffic = Traffic()

screen.listen()
screen.onkey(player.up, "w")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(traffic.pace)
    traffic.create_car()
    traffic.move()

    if player.ycor() > 280:
        player.refresh()
        scoreboard.update_scoreboard()
        traffic.pace_increase()

    for car in traffic.cars:
        if player.distance(car) < 40:
            scoreboard.gameover()
            game_is_on = False

    if len(traffic.cars) > 30:
        for i in range(10):
            traffic.remove()

screen.exitonclick()
