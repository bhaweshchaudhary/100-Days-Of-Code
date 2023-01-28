from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

mero_screen = Screen()
mero_screen.setup(width=600, height=600)
mero_screen.bgcolor("black")
mero_screen.title("Mero Snake Game")
mero_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

mero_screen.exitonclick()
