from turtle import Turtle, Screen

finger = Turtle()
finger.shape("turtle")
finger.color("green")

for i in range(10):
    finger.forward(5)
    finger.penup()
    finger.forward(5)
    finger.pendown()

screen = Screen()
screen.exitonclick()