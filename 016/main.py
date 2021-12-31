from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

timmy.shape("turtle")
timmy.color("DarkGreen")

for _ in range(1,11):
    timmy.forward(100)
    timmy.back(100)

my_screen.exitonclick()
