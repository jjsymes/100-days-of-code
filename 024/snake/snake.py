from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]
        self.next_heading = self.head.heading()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def move_forward(self):
        last_positions = []
        for segment in self.body_segments:
            last_positions.append(segment.pos())
        if self.next_heading == LEFT:
            self.left()
        elif self.next_heading == RIGHT:
            self.right()
        elif self.next_heading == UP:
            self.up()
        elif self.next_heading == DOWN:
            self.down()
        self.head.forward(MOVE_DISTANCE)
        for index, segment in enumerate(self.body_segments):
            if index != 0:
                self.body_segments[index].setposition(last_positions[index - 1])

    def right(self):
        self.head.setheading(RIGHT)

    def left(self):
        self.head.setheading(LEFT)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def set_heading_left(self):
        if self.head.heading() != RIGHT:
            self.next_heading = LEFT
    
    def set_heading_right(self):
        if self.head.heading() != LEFT:
            self.next_heading = RIGHT

    def set_heading_up(self):
        if self.head.heading() != DOWN:
            self.next_heading = UP

    def set_heading_down(self):
        if self.head.heading() != UP:
            self.next_heading = DOWN

    def add_segment(self, position):
        new_body_segment = Turtle(shape="square")
        new_body_segment.color("white")
        new_body_segment.speed(0)
        new_body_segment.penup()
        new_body_segment.setposition(position)
        new_body_segment.setheading(0)
        self.body_segments.append(new_body_segment)

    def extend(self):
        end_position = self.body_segments[-1].pos()
        self.add_segment(end_position)

    def reset(self):
        for segment in self.body_segments:
            segment.clear()
            segment.ht()
        self.__init__()

