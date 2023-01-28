from turtle import Turtle, Screen

mero_turtle = Turtle()
mero_turtle.shape("triangle")
mero_turtle.color("green")

for i in range(3):
    mero_turtle.color("green")
    mero_turtle.forward(100)
    mero_turtle.right(120)

for i in range(4):
    mero_turtle.color("navy")
    mero_turtle.forward(100)
    mero_turtle.right(90)

for i in range(5):
    mero_turtle.color("red")
    mero_turtle.forward(100)
    mero_turtle.right(72)

for i in range(6):
    mero_turtle.color("maroon")
    mero_turtle.forward(100)
    mero_turtle.right(60)

for i in range(8):
    mero_turtle.color("deep pink")
    mero_turtle.forward(100)
    mero_turtle.right(45)

for i in range(9):
    mero_turtle.color("blue violet")
    mero_turtle.forward(100)
    mero_turtle.right(40)

for i in range(10):
    mero_turtle.color("orange red")
    mero_turtle.forward(100)
    mero_turtle.right(36)

for i in range(12):
    mero_turtle.color("linen")
    mero_turtle.forward(100)
    mero_turtle.right(30)


mero_screen = Screen()
mero_screen.exitonclick()