import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

mero_screen = Screen()
mero_screen.setup(width=500, height=500)
user_bet = mero_screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "green", "blue", "purple", "yellow"]
y_position = [-90, -50, -10, 30, 70, 110]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=-y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 210:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color}  turtle is the winner.")
            else:
                print(f"You've lost! {winning_color}  turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)

mero_screen.exitonclick()
