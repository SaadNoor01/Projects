from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.board = Turtle()
        self.board.penup()
        self.board.color("white")
        self.board.hideturtle()
        self.hideturtle()
        self.board.goto(0, 270)
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())

        self.board.write(f"Score: {self.score}   High Score: {self.highscore}", False, "center",
                         ("Courier", 24, "normal"))

    def reset_sc(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def gameover(self):
        self.board.goto(0, 0)
        self.board.write("GAME OVER", False, "center", ("Courier", 24, "normal"))

    def update_scoreboard(self):
        self.board.clear()
        self.board.write(f"Score: {self.score}   High Score: {self.highscore}", False, "center",
                         ("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
