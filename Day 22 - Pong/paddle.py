from turtle import Turtle
class Paddle(Turtle):


    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.part = None
        self.paddle_part = None
        self.paddle_segment = []
        self.paddle(5, x_cor, y_cor)


    def paddle(self, difficulty, x_cor, y_cor):
        for _ in range(difficulty):
            self.paddle_part = Turtle()
            self.paddle_part.shape("square")
            self.paddle_part.setheading(90)
            if len(self.paddle_segment) == 0:
                self.paddle_part.setposition(x_cor, y_cor)
            else:
                self.paddle_part.setposition(x= x_cor, y = self.paddle_segment[-1].ycor()-20)
            self.paddle_part.width(20)
            self.paddle_part.color("white")
            self.paddle_part.penup()
            self.paddle_segment.append(self.paddle_part)


    def move_up(self):
        for segment in self.paddle_segment:
            if segment.ycor() > 260:
                return
        else:
            for part in self.paddle_segment:
                part.forward(20)


    def move_down(self):
        for segment in self.paddle_segment:
            if segment.ycor() < -260:
                return
        else:
            for part in self.paddle_segment:
                part.backward(20)


