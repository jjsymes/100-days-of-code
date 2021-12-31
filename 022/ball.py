from turtle import Turtle, update
from random import randint, random
from math import pi, cos, sin

MOVE_DISTANCE = 20
STARTING_X_POS = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.velocity = self._get_starting_velocity()
        self.penup()
        self.setposition((STARTING_X_POS, randint(-290, 290)))

    def _get_starting_velocity(self):
        speed = 400 
        # random angle, but never too vertical
        phi = 2 * pi * ((random() * 0.15) + 0.5 * randint(0, 1))
        vx = speed * cos(phi)
        vy = speed * sin(phi)
        return (vx, vy)

    def start_state(self):
        self.velocity = self._get_starting_velocity()
        self.setposition((STARTING_X_POS, randint(-290, 290)))

    def update_state(self, delta_t):
        self._update_position(delta_t)
        

    def _update_position(self, delta_t):
        last_position = self.position()
        new_position = (last_position[0] + self.velocity[0] * delta_t, last_position[1] + self.velocity[1] * delta_t)
        wall_collision = self._detect_wall_collision(new_position)
        if wall_collision:
            self._handle_wall_collision()

        self.setposition(new_position)

    def _detect_wall_collision(self, position):
        y_pos = position[1]
        if y_pos >= 285 or y_pos <= -285:
            return True
        else:
            return False

    def _handle_wall_collision(self):
        pre_collision_velocity = self.velocity
        new_velocity = (pre_collision_velocity[0], pre_collision_velocity[1] * -1)
        self.velocity = new_velocity

    def handle_paddle_collision(self):
        pre_collision_velocity = self.velocity
        new_velocity = (pre_collision_velocity[0] * -1.03, pre_collision_velocity[1])
        self.velocity = new_velocity


