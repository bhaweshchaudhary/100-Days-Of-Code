# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst_painting.jpeg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255)
tigress = turtle_module.Turtle()
tigress.speed("fastest")
tigress.hideturtle()
tigress.penup()

colors = [(196, 160, 119), (71, 92, 126), (144, 86, 57), (216, 210, 119), (140, 160, 189), (183, 146, 162)
          , (214, 61, 119), (65, 198, 119), (7, 4, 119), (195, 0, 1)]

tigress.setheading(225)
tigress.forward(300)
tigress.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tigress.dot(20, random.choice(colors))
    tigress.forward(50)
    if dot_count % 10 == 0:
        tigress.setheading(90)
        tigress.forward(50)
        tigress.setheading(180)
        tigress.forward(500)
        tigress.setheading(0)

mero_screen = Screen()
mero_screen.exitonclick()