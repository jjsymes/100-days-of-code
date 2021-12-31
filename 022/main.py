from turtle import Turtle, Screen
from time import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

PHYSICS_REFRESH_RATE = 120
wait_time = 1/PHYSICS_REFRESH_RATE

def draw_dashed_line(turtle: Turtle, length, down_length=5, up_length=5):
    distance_travelled = 0
    cycles = 0
    cycle_distance = down_length + up_length

    if length > 0:
        cycles = length // cycle_distance
    for _ in range(cycles):
        turtle.pendown()
        turtle.forward(down_length)
        turtle.penup()
        turtle.forward(up_length)
    
    distance_travelled = cycle_distance * cycles
    length_remaining = length - distance_travelled
    if length_remaining <= down_length:
        down_length_remaining = length_remaining
        up_length_remaining = 0
    else:
        down_length_remaining = down_length
        up_length_remaining = length_remaining - down_length_remaining

    turtle.forward(down_length_remaining)
    turtle.penup()
    turtle.forward(up_length_remaining)
    turtle.pendown()

def draw_level():
    level_drawer = Turtle()
    level_drawer.pencolor("white")
    level_drawer.penup()
    level_drawer.hideturtle()
    level_drawer.speed("fastest")
    level_drawer.goto(0, -300)
    level_drawer.setheading(90)
    level_drawer.pensize(2)
    draw_dashed_line(level_drawer, 600, 10, 7)

def ball_player_1_paddle_collision():
    player_1_paddle_pos = player_1_paddle.pos()
    ball_pos = ball.pos()
    x_distance_player_1 = player_1_paddle_pos[0] - ball_pos[0]
    y_distance_player_1 = player_1_paddle_pos[1] - ball_pos[1]
    if x_distance_player_1 < 0:
        x_distance_player_1 = x_distance_player_1 * -1
    if (x_distance_player_1 < 15 and x_distance_player_1 >= 0 and y_distance_player_1 < 50 and y_distance_player_1 > -50):
        return True
    else:
        return False

def ball_player_2_paddle_collision():
    player_2_paddle_pos = player_2_paddle.pos()
    ball_pos = ball.pos()
    x_distance_player_2 = player_2_paddle_pos[0] - ball_pos[0]
    y_distance_player_2 = player_2_paddle_pos[1] - ball_pos[1]
    if x_distance_player_2 < 0:
        x_distance_player_2 = x_distance_player_2 * -1
    if (x_distance_player_2 < 15 and x_distance_player_2 >= 0 and y_distance_player_2 < 50 and y_distance_player_2 > -50):
        return True
    else:
        return False

def ball_paddle_collision():
    if ball_player_1_paddle_collision() or ball_player_2_paddle_collision():
        return True
    else:
        return False

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

draw_level()
scoreboard = Scoreboard()
player_1_paddle = Paddle(-350)
player_2_paddle = Paddle(350)
ball = Ball()

game_in_progress = True

screen.update()

screen.onkey(key="w", fun=player_1_paddle.up)
screen.onkey(key="s", fun=player_1_paddle.down)
screen.onkey(key="Up", fun=player_2_paddle.up)
screen.onkey(key="Down", fun=player_2_paddle.down)

time_of_last_frame = time()
while game_in_progress == True:
    screen.update()
    if time() - time_of_last_frame > wait_time:
        ball.update_state(wait_time)
        if ball_paddle_collision():
            ball.handle_paddle_collision()
        if ball.position()[0] > 400:
            scoreboard.increase_score("player_1")
            ball.start_state()
        elif ball.position()[0] < -400:
            scoreboard.increase_score("player_2")
            ball.start_state()
        
        if scoreboard.player_1_score >= 7 or scoreboard.player_2_score >= 7:
            game_in_progress = False
            scoreboard.game_over()
    else:
        pass


screen.exitonclick()
