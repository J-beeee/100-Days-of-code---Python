from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-240, 240)
        self.pencolor("red")

    def level(self, level):
        self.clear()
        self.write(arg= f"Level:{level}", align="center",font = ("Courier", 20, "normal"))