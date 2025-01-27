from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.8)
        self.color("white")
        self.penup()
        self.speed(0)
        self.x_move = 10
        self.y_move = 10
        self.pace = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def pace_increase(self):
        self.pace -= (self.pace / 8)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.pace = 0.1
        self.bounce_x()
