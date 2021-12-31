from turtle import Turtle

FONT = "courier"
SIZE = "21"
STYLE = "bold"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=(FONT, SIZE, STYLE))

    def increase_score(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=(FONT, SIZE))
