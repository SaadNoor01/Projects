from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.75)
        self.color("green")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto(x=0, y=-270)

    def up(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() + 20)

    def refresh(self):
        self.goto(0, -270)
