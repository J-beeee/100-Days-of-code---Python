import time
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.last_move = 0
        self.time = time.time()

    def move_north(self):
        if self.ycor() >=280:
            return
        else:
            if self.input_delay():
                self.forward(20)

    def move_south(self):
        if self.ycor() <= -280:
            return
        else:
            if self.input_delay():
                self.backward(20)

    def move_west(self):
        if self.xcor() <= -280:
            return
        else:
            if self.input_delay():
                self.setheading(180)
                self.forward(20)
                self.setheading(90)

    def move_east(self):
        if self.xcor() >= 280:
            return
        else:
            if self.input_delay():
                self.setheading(0)
                self.forward(20)
                self.setheading(90)


    def input_delay(self):
        if time.time() - self.last_move < 0.5:
            return False
        else:
            self.last_move = time.time()
            return True