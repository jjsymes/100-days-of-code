from turtle import Turtle, Screen, distance
import random

def create_turtle(color):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    return turtle

def is_turtle_at_finish_line(turtle: Turtle):
    finish_line = 200
    if turtle.xcor() >= finish_line:
        is_at_finish_line = True
    else:
        is_at_finish_line = False
    return is_at_finish_line

race_in_progress = False
winner = ""
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for color in colors:
    turtle = create_turtle(color)
    turtles.append(turtle)

y = -125
for turtle in turtles:
    turtle.goto(x=-230, y=y)
    y += 50

if user_bet:
    race_in_progress = True

while race_in_progress:
    for turtle in turtles:
        distance_left = 200 - turtle.xcor()
        if distance_left < 10:
            random_distance = random.randint(0, distance_left)
        else:
            random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if is_turtle_at_finish_line(turtle):
            race_in_progress = False
            winner = turtle.pencolor()
            break

if user_bet == winner:
    print(f"Winner! {winner.capitalize()} won the race!")
else:
    print(f"You lose, {winner.capitalize()} won the race!")


screen.exitonclick()
