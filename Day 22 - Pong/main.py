
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from field import Field

s = Screen()
s.title("PONG")
s.setup(width=800, height=600)
s.bgcolor("black")
s.listen()
s.tracer(False)
scoreboard = Scoreboard()
scoreboard.score()
field = Field()
field.field()

paddle_east = Paddle(350,0)
paddle_west = Paddle(-350,0)
ball = Ball()
s.onkeypress(fun=paddle_east.move_up, key="Up")
s.onkeypress(fun=paddle_east.move_down, key="Down")
s.onkeypress(fun=paddle_west.move_up, key="w")
s.onkeypress(fun=paddle_west.move_down, key="s")
s.update()
game_on = True

scoreboard.score()
while game_on:
    s.update()
    ball.move()
    if ball.xcor() <= -380:
        scoreboard.score_east += 1
        scoreboard.score()
    elif ball.xcor() >= 380:
        scoreboard.score_west += 1
        scoreboard.score()
    for segment in paddle_west.paddle_segment:
        if ball.distance(segment) < 20:
            ball.bounce_paddle(paddle_y=paddle_west.paddle_segment[2].ycor())
    for segment in paddle_east.paddle_segment:
        if ball.distance(segment) < 20:
            ball.bounce_paddle(paddle_y=paddle_east.paddle_segment[2].ycor())








s.exitonclick()