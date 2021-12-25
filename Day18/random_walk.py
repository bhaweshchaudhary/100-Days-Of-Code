from turtle import Turtle, Screen
import random

panda = Turtle()
colours = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
panda.pensize(15)
panda.speed("fastest")

for _ in range(200):
    panda.color(random.choice(colours))
    panda.forward(30)
    panda.setheading(random.choice(directions))

mero_screen = Screen()
mero_screen.exitonclick()