
from time import time, sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

GAME_SPEED = 10
wait_time = 1/GAME_SPEED

def out_of_bounds():
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        return True
    else:
        return False

def body_collision():
    has_collided = False
    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            has_collided = True
    return has_collided

def head_at_food():
    if snake.head.distance(food) < 15:
        return True
    else:
        return False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="a", fun=snake.set_heading_left)
screen.onkey(key="d", fun=snake.set_heading_right)
screen.onkey(key="w", fun=snake.set_heading_up)
screen.onkey(key="s", fun=snake.set_heading_down)
screen.onkey(key="Left", fun=snake.set_heading_left)
screen.onkey(key="Right", fun=snake.set_heading_right)
screen.onkey(key="Up", fun=snake.set_heading_up)
screen.onkey(key="Down", fun=snake.set_heading_down)

game_in_progress = True

screen.update()

time_of_last_frame = time()
while game_in_progress == True:
    if time() - time_of_last_frame > wait_time:
        snake.move_forward()
        if head_at_food():
            scoreboard.increase_score()
            food.refresh()
            snake.extend()
        time_of_last_frame = time()
        screen.update()
    else:
        pass
    
    if out_of_bounds() or body_collision():
        scoreboard.game_over()
        sleep(3)
        scoreboard.reset()
        snake.reset()


screen.exitonclick()
