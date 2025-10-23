from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.color("white")
        try:
            file = open("scoreboard.txt", mode="r")
            self.high_score = file.read()
            self.high_score = int(self.high_score)
            file.close()
        except FileNotFoundError:
            file = open("scoreboard.txt", mode="w")
            self.high_score = 0
            file.close()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", font=("Arial", 20, "normal"))


    def new_score(self):
        self.score += 1
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scoreboard.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", font=("Arial", 20, "normal"))

    #def game_over(self):
    #    self.setposition(0,0)
    #    self.write(f"GAME OVER", False, "center",font=("Arial", 20, "normal"))