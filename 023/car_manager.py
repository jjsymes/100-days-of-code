from turtle import Turtle, register_shape
from random import choice, randint, random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SHAPE_CORS=((-7,20),(7,20),(7,-20),(-7,-20))

register_shape("rectangle", SHAPE_CORS)

class Car(Turtle):
    def __init__(self, move_speed):
        super().__init__()
        self.shape("rectangle")
        self.color(choice(COLORS))
        self.move_speed = move_speed
        self.penup()
        self.setposition((350, randint(-23, 23) * 10))

    def move_forward(self):
        old_position = self.position()
        new_position = (old_position[0] - self.move_speed, old_position[1])
        self.setposition(new_position)



class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.initial_cars()

    def update(self):
        if len(self.cars) < 20:
            self.new_car()
        for car in self.cars:
            car.move_forward()
            if car.position()[0] < -310:
                car.clear()
                car.ht()
                self.cars.remove(car)

    def new_car(self):
        self.cars.append(Car(self.move_distance))

    def increase_difficulty(self):
        self.move_distance += MOVE_INCREMENT
        self.initial_cars()

    def initial_cars(self):
        for car in self.cars:
            car.clear()
            car.ht()
        self.cars = []
        for _ in range(20):
            car = Car(self.move_distance)
            car_position = car.position()
            random_x_position = randint(-300, 300)
            car.setposition((random_x_position, car_position[1]))
            self.cars.append(car)
