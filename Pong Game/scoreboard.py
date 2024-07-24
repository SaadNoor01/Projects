from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.score()

    def score(self):
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))

    def p1_score_update(self):
        self.p1_score += 1
        self.clear()
        self.score()

    def p2_score_update(self):
        self.p2_score += 1
        self.clear()
        self.score()

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"{player} Wins!", align="center", font=("Courier", 30, "bold"))
