from turtle import Turtle
class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.pensize(5)

    def field(self):
        self.goto(10,300)
        self.pendown()
        self.setheading(270)
        while self.ycor() >-320:
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()