from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score_west = 0
        self.score_east = 0

    def score(self):
        self.clear()
        self.penup()
        self.goto(-50, 250)
        self.write(f"{self.score_west}",False,"left",('Arial', 22, 'normal'))
        self.goto(50, 250)
        self.write(f"{self.score_east}", False, "left", ("Arial", 22, "normal"))
