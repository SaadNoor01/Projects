from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.board = Turtle()
        self.board.penup()
        self.board.color("white")
        self.board.hideturtle()
        self.board.goto(-270, 270)
        self.level = 1
        self.board.write(f"Level: {self.level}", False, "center", ("Courier", 24, "normal"))


    def gameover(self):
        self.board.goto(0, 0)
        self.board.write("GAME OVER", False, "center", ("Courier", 24, "normal"))


    def update_scoreboard(self):
        self.board.clear()
        self.level += 1
        self.board.write(f"Level: {self.level}", False, "center", ("Courier", 24, "normal"))
