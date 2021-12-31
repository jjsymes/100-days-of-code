import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard


def player_collistion_with_car(player: Player, car: Car):
    collision = False
    car_position = car.position()
    player_position = player.position()
    object_distance = player_position - car_position
    object_distance = (abs(object_distance[0]), abs(object_distance[1]))
    if object_distance[0] < 30 and object_distance[1] < 21:
        collision = True
    return collision



screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(key="w", fun=player.move)
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.update()
    if player.at_finish_line():
        player.reset_position()
        scoreboard.increase_score()
        car_manager.increase_difficulty()

    for car in car_manager.cars:
        if player.distance(car) < 40:
            if player_collistion_with_car(player, car):
                game_is_on = False
    screen.update()

scoreboard.game_over()
screen.update()
screen.exitonclick()