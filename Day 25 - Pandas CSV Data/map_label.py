from turtle import Turtle
FONT = ("Arial", 14, "bold")
class Label(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("red")
    def add_label(self, state_name,x_cord, y_cord):
        self.goto(x_cord, y_cord)
        self.write(arg=state_name, align="center", font=FONT)