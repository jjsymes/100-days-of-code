import turtle
import pandas

def reveal_text(turtle, text, position):
    turtle.goto(position)
    turtle.write(text)


image = "blank_states_img.gif"
to_learn_file = "states_to_learn.csv"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)

level_drawer = turtle.Turtle()
level_drawer.pencolor("black")
level_drawer.penup()
level_drawer.hideturtle()
level_drawer.speed("fastest")

turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
number_of_states = len(state_data)
states = state_data["state"].to_list()
correct_answers = 0

while len(states) > 0:
    answer_state = screen.textinput(title=f"{correct_answers}/{number_of_states} States Correct", prompt="What's another state's name?")
    if answer_state:
        answer_state = answer_state.title()
    if answer_state in states:
        select_state = state_data[state_data["state"] == answer_state]
        state_position = (int(select_state.x), int(select_state.y))
        reveal_text(level_drawer, select_state.state.item(), state_position)
        states.remove(answer_state)
        correct_answers += 1
    elif answer_state == "Exit":
        for state in states:
            select_state = state_data[state_data["state"] == state]
            state_position = (int(select_state.x), int(select_state.y))
            reveal_text(level_drawer, select_state.state.item(), state_position)
        
        to_learn_dataframe = pandas.DataFrame(states)
        to_learn_dataframe.to_csv(to_learn_file)
        break

turtle.mainloop()