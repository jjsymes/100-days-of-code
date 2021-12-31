
import turtle as t
import random, os
import colorgram

path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))

colors = colorgram.extract(f'{path}/image.jpg', 17)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

for _ in range(5):
    rgb_colors.pop(0)

color_list = rgb_colors

def hirst_painting(turtle: t.Turtle, dot_size=20, rows=10, columns=10, spacing=50):
    turtle.penup()
    for _ in range(rows):
        for _ in range(columns):
            turtle.dot(dot_size, random.choice(color_list))
            turtle.forward(spacing)
        turtle.backward(spacing * columns)
        turtle.setheading(90)
        turtle.forward(spacing)
        turtle.setheading(0)

screen = t.Screen()
turtle = t.Turtle()
turtle.hideturtle()
turtle.speed("fastest")
screen.colormode(255)
turtle.penup()

# Get into bottom left position
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)

# draw painting
hirst_painting(turtle)

screen.exitonclick()
