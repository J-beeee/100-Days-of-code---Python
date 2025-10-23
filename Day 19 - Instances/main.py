from turtle import Turtle, Screen

t = Turtle()
s = Screen()

#def move_right():
#    t.setheading(0)
#    t.forward(10)
#def move_left():
#    t.setheading(180)
#    t.forward(10)
#def move_up():
#    t.setheading(90)
#    t.forward(10)
#def move_down():
#    t.setheading(270)
#    t.forward(10)
#

def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
def turn_cc():
    t.left(10)
def turn_c():
    t.right(10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.onkey(fun=move_forward
        ,key="w")
s.onkey(fun=move_backward
        ,key="s")
s.onkey(fun=turn_cc
        ,key="a")
s.onkey(fun=turn_c
        ,key="d")
s.onkey(fun=clear
        ,key="c")
s.listen()
#s.onkey(move_right, "Right")
#s.onkey(move_left, "Left")
#s.onkey(move_up, "Up")
#s.onkey(move_down, "Down")



s.exitonclick()

