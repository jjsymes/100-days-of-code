from turtle import Turtle

FONT = "courier"
SIZE = "40"
STYLE = ""

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 250)
        self.player_1_score = 0
        self.player_2_score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.player_1_score}\t{self.player_2_score}", align="center", font=(FONT, SIZE, STYLE))

    def increase_score(self, player):
        if player == "player_1":
            self.player_1_score += 1
        elif player == "player_2":
            self.player_2_score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=(FONT, SIZE))
