import turtle as t
import random

def draw_circle(turtle, radius):
    turtle.circle(radius)

def spirograph(turtle: t.Turtle, radius, circle_count):
    angle_tilt = 360 / circle_count
    for _ in range(circle_count):
        turtle.color(random_color())
        draw_circle(turtle, radius)
        turtle.left(angle_tilt)
    turtle.setheading(0)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

turtle = t.Turtle()
turtle.speed("fastest")
spirograph(turtle, 90, 100)

screen = t.Screen()
screen.exitonclick()