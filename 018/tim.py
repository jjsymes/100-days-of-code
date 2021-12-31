#####Turtle Intro######

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
# tim.forward(100)
# tim.backward(200)
# tim.right(90)
# tim.left(180)
# tim.setheading(0)


######## Challenge 1 - Draw a Square ############

def draw_square(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_dashed_line(turtle, length, down_length=5, up_length=5):
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

draw_square(tim, 50)
draw_dashed_line(tim, 99)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def draw_shape(turtle: t.Turtle, side_count, side_length=100, color="random"):
    if color == "random":
        color = random_color()
    turtle.pencolor(color)

    angle = 360 / side_count
    for _ in range(side_count):
        turtle.forward(side_length)
        turtle.right(angle)

for shape_side_count in range(3, 11):
    draw_shape(tim, shape_side_count)

def random_walk(turtle, cycles=100, forward_distance=15, pen_thickness=5, speed=10):
    turtle.speed(speed)
    turtle.pensize(pen_thickness)
    for _ in range(cycles):
        color = random_color()
        direction = random.choice([0, 90, 180, 270])
        turtle.pencolor(color)
        turtle.setheading(direction)
        turtle.forward(forward_distance)


random_walk(tim)