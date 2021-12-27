from turtle import Turtle, Screen
from snake import Snake
import time

mero_screen = Screen()
mero_screen.setup(width=800, height=800)
mero_screen.bgcolor("black")
mero_screen.title("Mero Snake Game")
mero_screen.tracer(0)

snake = Snake()

mero_screen.listen()
mero_screen.onkey(snake.up, "Up")
mero_screen.onkey(snake.down, "Down")
mero_screen.onkey(snake.left, "Left")
mero_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    mero_screen.update()
    time.sleep(0.1)
    snake.move()


mero_screen.exitonclick()