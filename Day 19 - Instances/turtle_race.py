import random
from turtle import Turtle, Screen
color = ["blue", "red", "purple", "pink", "black", "green"]
s = Screen()
s.setup(width=500, height=400)
all_turtles = []
is_race_on = False
x = -230
y = -90
for i in color:
    x = -230
    y += 30
    t = Turtle(shape="turtle")
    t.penup()
    t.color(i)
    t.setposition(x, y)
    all_turtles.append(t)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")





s.exitonclick()