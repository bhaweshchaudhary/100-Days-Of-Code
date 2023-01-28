import turtle
from turtle import Turtle, Screen
import random

mero_kachuwa = Turtle()
turtle.colormode(255)
mero_kachuwa.shape("turtle")


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


mero_kachuwa.speed("fastest")


def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        mero_kachuwa.color(random_colors())
        mero_kachuwa.circle(100)
        mero_kachuwa.setheading(mero_kachuwa.heading() + size_of_gap)
        mero_kachuwa.circle(100)


spirograph(1)

mero_screen = Screen()
mero_screen.exitonclick()
