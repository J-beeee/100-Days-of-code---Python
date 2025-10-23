from turtle import Turtle

class Map(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300,-280)
        self.setheading(0)
        self.pensize(20)
        self.draw_map()
    def draw_green(self):
        self.pendown()
        self.color("green")
        self.forward(600)
        self.penup()
        self.goto(self.xcor() - 600, self.ycor() + 20)
    def draw_grey(self):
        self.pendown()
        self.color("grey")
        self.forward(600)
        self.penup()
        self.goto(self.xcor() - 600, self.ycor() + 20)
    def draw_white(self):
        self.goto(self.xcor(), self.ycor() - 10)
        self.pendown()
        self.color("black")
        self.pensize(5)
        while self.xcor() < 300:
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()
        self.penup()
        self.goto(self.xcor() - 600, self.ycor() + 10)
        self.pensize(20)
    def draw_map(self):
        while self.ycor() < 320:
            if self.ycor() <= -240 or self.ycor() >= 240:
                self.draw_green()
            else:
                self.draw_grey()
                self.draw_grey()
                self.draw_white()
                self.draw_grey()
                self.draw_grey()
                self.draw_green()
                self.draw_green()

