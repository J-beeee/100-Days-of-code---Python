import random
from turtle import Turtle

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_parts = None
        self.car_list = []


    def car_spawn(self):
        car = []
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for i in range(2):
            self.car_parts = Turtle(shape="square")
            self.car_parts.penup()
            self.car_parts.color(color)
            car.append(self.car_parts)
            if i == 0:
                self.car_parts.setposition(400, 400)
            elif i == 1:
                self.car_parts.setposition(x=car[0].xcor() - 20, y=car[0].ycor())
        self.car_list.append(car)

    def car_move(self):
        car_head = self.car_list[-1][0]
        car_back = self.car_list[-1][1]
        sides = [-320, 320]
        random_side = random.choice(sides)
        random_height = [random.randint(-220, -160), random.randint(-100, -40), random.randint(20, 80),
                         random.randint(140, 200)]
        random_height = random.choice(random_height)
        if random_side > 0:
            car_head.goto(random_side, random_height)
            car_head.setheading(180)
            car_back.goto(random_side + 20, random_height)
            car_back.setheading(180)
        elif random_side < 0:
            car_head.goto(random_side, random_height)
            car_head.setheading(0)
            car_back.goto(random_side -20, random_height)
            car_back.setheading(0)

    def car_drive(self):
        for car in self.car_list:
            for i in(0,1):
                car[i].speed(0.1)
                car[i].forward(10)
                if car[i].xcor() <= -360 or car[i].xcor() >= 360:
                    self.delete_car(car[i])

    def delete_car(self, car_given):
        for car in self.car_list:
            for part in car:
                if part == car_given:
                    self.car_list.remove(car)

        car_given.clear()
        del car_given

