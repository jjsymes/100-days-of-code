from turtle import Turtle

FONT = "courier"
SIZE = "21"
STYLE = "bold"
DATA_FILE="data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}\t High Score: {self.high_score}", align="center", font=(FONT, SIZE, STYLE))

    def read_high_score(self):
        try:
            with open(DATA_FILE, mode="r") as f:
                high_score = f.read()
                high_score = int(high_score)
                self.high_score = high_score
        except FileNotFoundError:
            with open(DATA_FILE, mode="w") as f:
                f.write("0")

    def save_high_score(self):
        with open(DATA_FILE, mode="w") as f:
            f.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.print_score()

    def reset(self):
        self.goto(0, 270)
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=(FONT, SIZE))

