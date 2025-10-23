import time
from turtle import Screen
from car import Car
from player import Player
from map import Map
from player_info import Info
from scoreboard import Scoreboard


s = Screen()
s.colormode(255)
s.setup(width=600, height=600)
s.tracer(0)
s.listen()
background = Map()
car_manager = Car()
info_manager = Info()
s.update()
alive = True
last_spawn_time = 0
print_time = 0
player = Player()
s.onkeypress(fun=player.move_north,key="Up")
s.onkeypress(fun=player.move_south,key="Down")
s.onkeypress(fun=player.move_west,key="Left")
s.onkeypress(fun=player.move_east,key="Right")

level = 1
car_respawn = 0.5
lvl_scoreboard = Scoreboard()
lvl_scoreboard.level(level)
while alive:
    current_time = time.time()
    time.sleep(0.1)
    s.update()
    if current_time - last_spawn_time > car_respawn:
        car_manager.car_spawn()
        car_manager.car_move()
        last_spawn_time = current_time
    car_manager.car_drive()

    for car in car_manager.car_list:
        for part in car:
            if player.distance(part) <= 20:
                info_manager.restart()
                print_time = time.time()
                player.goto(0, -280)

    if print_time != 0 and time.time() - print_time >= 10:
        info_manager.clear_screen()
        print_time = 0
    if player.ycor() >= 280:
        info_manager.won()
        print_time = time.time()
        player.goto(0, -280)
        car_respawn += (-0.1)
        print(car_respawn)
        level += 1
        lvl_scoreboard.level(level)


s.exitonclick()