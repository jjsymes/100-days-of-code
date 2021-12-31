from random import randint
from turtle import Turtle, register_shape

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
PADDLE_CORS=((-50,10),(50,10),(50,-10),(-50,-10))

register_shape("rectangle", PADDLE_CORS)

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.shape("rectangle")
        self.color("white")
        self.speed(0)
        self.penup()
        self.setposition((x_pos, 0))

    def up(self):
        y_pos = self.ycor()
        if y_pos < 260:
            new_y_pos = y_pos + 20
            self.setposition((self.x_pos, new_y_pos))
        else:
            pass

    def down(self):
        y_pos = self.ycor()
        if y_pos > -260:
            new_y_pos = y_pos - 20
            self.setposition((self.x_pos, new_y_pos))
        else:
            pass





