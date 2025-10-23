import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(3)
screen = Screen()
screen.colormode(255)
timmy.speed(10)
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

i= 2
while i < 1000:
    i += 1
    timmy.pencolor(random_color())
    for _ in range (i):
        timmy.right(180/i*2)
        timmy.circle(80)





screen.exitonclick()