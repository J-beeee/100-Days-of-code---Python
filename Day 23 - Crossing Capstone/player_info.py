import time
from turtle import Turtle

class Info(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.pencolor("red")


    def restart(self):
        self.write(arg= "Ouch - Try again!", align="center",font = ("Courier", 24, "normal"))

    def won(self):
        self.write(arg="YOU WON", align="center", font=("Courier", 24, "normal"))

    def clear_screen(self):
        self.clear()
