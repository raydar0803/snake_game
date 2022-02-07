# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

food = Food()
snake = Snake()
screen = Screen()
score = Score()
score.keep_score()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        game_is_on = False
        game_over = Turtle()
        game_over.hideturtle()
        game_over.color("white")
        game_over.write("Game Over.", move=False, align="center", font=("Arial", 18, "normal"))

    # Detect collision with tail
    for segment in snake.segments[1:len(snake.segments)]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            game_over = Turtle()
            game_over.hideturtle()
            game_over.color("white")
            game_over.write("Game Over.", move=False, align="center", font=("Arial", 18, "normal"))


screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
