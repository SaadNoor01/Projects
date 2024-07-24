from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p2.up, "Left")
screen.onkey(p2.down, "Right")
screen.onkey(p1.up, "a")
screen.onkey(p1.down, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.pace)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(p2) < 50:
        ball.pace_increase()
        ball.bounce_x()

    if ball.xcor() < -330 and ball.distance(p1) < 50:
        ball.pace_increase()
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.p1_score_update()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.p2_score_update()

    if scoreboard.p1_score >= 5:
        game_is_on = False
        scoreboard.game_over(player="Player 1")

    if scoreboard.p2_score >= 5:
        game_is_on = False
        scoreboard.game_over(player="Player 2")

screen.exitonclick()
