import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(3)
screen = Screen()
screen.colormode(255)

i= 2
while i < 1000:
    i += 1
    timmy.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    for _ in range (i):
        timmy.right(180/i*2)
        timmy.forward(100)





screen.exitonclick()