from turtle import Turtle, Screen

mero_screen = Screen()
mero_screen.setup(width=800, height=600)
mero_screen.bgcolor("black")
mero_screen.title("Mero Pong Game")
mero_screen.tracer(0)

paddle = Turtle(shape="square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(x=paddle.xcor(), y=new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(x=paddle.xcor(), y=new_y)


mero_screen.listen()
mero_screen.onkey(go_up, "Up")
mero_screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    mero_screen.update()

mero_screen.exitonclick()
