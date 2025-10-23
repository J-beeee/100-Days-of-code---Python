from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake")
s.tracer(0)
s.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.onkey(fun=snake.turn_north
            , key="Up")
s.onkey(fun=snake.turn_south
            ,key="Down")
s.onkey(fun=snake.turn_east
        , key="Right")
s.onkey(fun=snake.turn_west
        , key="Left")

s.update()
game_over = False
i= 0
while not game_over:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment(1)
        scoreboard.new_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.snake_tail_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()











s.exitonclick()