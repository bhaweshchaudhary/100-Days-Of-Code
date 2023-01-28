import turtle
import pandas

mero_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state name?").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    if answer_state == "Exit":
        # missing_states = []
        # for states in all_states:
        #     if states not in guessed_state:
        #         missing_states.append(states)
        missing_states = [states for states in all_states if states not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
