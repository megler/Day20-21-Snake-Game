# snakeGame.py
#
# Python Bootcamp Day 20-21 - Snake Game
# Usage:
#      The classic Snake game. Eat as much as you can without touching the
#      wall or yourself. Use the arrow keys to move your snake.
#
#
# Marceia Egler Nov 8, 2021

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Screen setup

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0, 0)

# Initialize scoreboard
scoreboard = Scoreboard()

# Initialize Food
food = Food()

# Draw opening snake body
snakes = Snake()
screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    # Detect collision with food
    if snakes.head.distance(food) < 15:
        food.refresh()
        snakes.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snakes.head.xcor() > 290
        or snakes.head.xcor() < -290
        or snakes.head.ycor() > 290
        or snakes.head.ycor() < -290
    ):
        scoreboard.reset()
        snakes.reset()

    # Detect collision with tail
    for segment in snakes.segments[1:]:
        if snakes.head.distance(segment) < 10:
            scoreboard.reset()
            snakes.reset()


screen.exitonclick()
