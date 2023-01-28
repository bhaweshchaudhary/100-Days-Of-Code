from turtle import Turtle, Screen

po = Turtle()
tigress = Screen()


def move_forward():
    po.forward(15)


def move_backward():
    po.back(15)


def turn_right():
    new_heading = po.heading() - 10
    po.setheading(new_heading)


def turn_left():
    new_heading = po.heading() + 10
    po.setheading(new_heading)


def clear():
    po.clear()
    po.penup()
    po.home()
    po.pendown()


tigress.listen()
tigress.onkey(fun=move_forward, key="w")
tigress.onkey(fun=move_backward, key="s")
tigress.onkey(fun=turn_left, key="a")
tigress.onkey(fun=turn_right, key="d")
tigress.onkey(fun=clear, key="c")
tigress.exitonclick()
