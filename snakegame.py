from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)

screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.collision():
        score.game_over()
        snake.reset()

    if snake.head.distance(food) < 15:
        snake.add_segment()
        score.add_score()
        food.refresh()

screen.exitonclick()