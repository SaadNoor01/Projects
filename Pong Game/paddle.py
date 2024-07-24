from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 0.5)
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(position)

    def up(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() - 20)
