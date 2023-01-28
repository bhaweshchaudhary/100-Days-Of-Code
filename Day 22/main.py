from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

mero_screen = Screen()
mero_screen.setup(width=800, height=600)
mero_screen.bgcolor("black")
mero_screen.title("Mero Pong Game")
mero_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

mero_screen.listen()
mero_screen.onkey(r_paddle.go_up, "Up")
mero_screen.onkey(r_paddle.go_down, "Down")
mero_screen.onkey(l_paddle.go_up, "w")
mero_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    mero_screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R_Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L_Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

mero_screen.exitonclick()
