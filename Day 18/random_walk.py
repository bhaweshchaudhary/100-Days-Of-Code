import turtle as t
import random

panda = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


directions = [0, 90, 180, 270]
panda.pensize(15)
panda.speed("fastest")

for _ in range(200):
    panda.color(random_color())
    panda.forward(30)
    panda.setheading(random.choice(directions))

