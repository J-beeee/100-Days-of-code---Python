import random
import time
from turtle import Turtle

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,0)
        self.color("white")
        self.setheading(random.randint(-1,360))
        self.speed = 0.198
        self.last_bounce_time = 0

    def move(self):
        """
        :return:Is moving the ball in the range of the screen
        """
        if self.xcor() > 380 or self.xcor() < -380:
            time.sleep(3)
            if self.speed >= 0.4: self.speed = 0.1
            return self.goto(0,0), self.setheading(random.randint(-1,360))
        elif self.ycor() > 280 or self.ycor() < -280:
            self.bounce_wall()
            return None
        else:
            self.forward(self.speed)
            return None

    def bounce_wall(self):
        self.setheading(360 - self.heading())
        self.speed *= 1.05
        self.forward(self.speed)
        if self.speed >= 1.5:
            self.speed = 0.1

    def bounce_paddle(self, paddle_y):
        current_time = time.time()
        if current_time - self.last_bounce_time<0.5:
            return
        self.last_bounce_time = current_time
        offset = (self.ycor() - paddle_y) *0.1
        if self.heading()> 90 < 270:
            self.setheading((180 - self.heading())+offset)
            self.speed *= 1.05
            self.forward(self.speed)
        elif self.heading()< 89:
            self.setheading((90 + self.heading())+offset)
            self.speed *= 1.05
            self.forward(self.speed)
        else:
            self.setheading((self.heading()- 90)+offset)
            self.speed *= 1.05
            self.forward(self.speed)
