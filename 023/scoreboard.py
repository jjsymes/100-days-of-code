from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(-280, 260)
        self.level = 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=(FONT))
