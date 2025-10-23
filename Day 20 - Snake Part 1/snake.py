from turtle import Turtle
MOVE_DISTANCE = 20
X_START_POSITION = 0
Y_START_POSITON = 0
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0
class Snake:

    def __init__(self):
        self.snake_tail_list = []
        self.create_head()
        self.add_segment(2)
        self.head = self.snake_tail_list[0]

    def create_head(self):
        snake_head = Turtle(shape="square")
        snake_head.penup()
        snake_head.color("white")
        snake_head.teleport(X_START_POSITION, Y_START_POSITON)
        self.snake_tail_list.append(snake_head)
        snake_head.speed("slowest")

    def add_segment(self, tail_part):
        for _ in range(tail_part):
            t = Turtle(shape="square")
            t.penup()
            t.goto(self.snake_tail_list[-1].position())
            t.color("white")
            self.snake_tail_list.append(t)

    def reset(self):
        for seg in self.snake_tail_list:
            seg.goto(1111,1111)
        self.snake_tail_list.clear()
        self.__init__()

    def move(self):
        for snake_tail in range(len(self.snake_tail_list) - 1, 0, -1):
            new_x = self.snake_tail_list[snake_tail - 1].xcor()
            new_y = self.snake_tail_list[snake_tail - 1].ycor()
            self.snake_tail_list[snake_tail].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
    def turn_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
    def turn_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)
    def turn_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)