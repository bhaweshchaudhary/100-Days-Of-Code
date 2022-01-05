from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

mero_screen = Screen()
mero_screen.setup(width=800, height=600)
mero_screen.bgcolor("black")
mero_screen.title("Mero Pong Game")
mero_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

mero_screen.listen()
mero_screen.onkey(r_paddle.go_up, "Up")
mero_screen.onkey(r_paddle.go_down, "Down")
mero_screen.onkey(l_paddle.go_up, "w")
mero_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    mero_screen.update()
    ball.move()

#     Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce()

mero_screen.exitonclick()
