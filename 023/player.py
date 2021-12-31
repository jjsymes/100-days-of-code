from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.speed(0)
        self.penup()
        print(self.shapesize())
        self.reset_position()

    def move(self):
        old_position = self.position()
        new_position = (old_position[0], old_position[1] + MOVE_DISTANCE)
        self.setposition(new_position)

    def reset_position(self):
        self.setposition(STARTING_POSITION)

    def at_finish_line(self):
        is_at_finish_line = False
        position = self.position()
        y_pos = position[1]
        if y_pos >= FINISH_LINE_Y:
            is_at_finish_line = True
        return is_at_finish_line
