'''url = https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if not right_is_clear() and front_is_clear():
        move()
    elif right_is_clear() and wall_in_front():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif right_is_clear() and not wall_in_front():
        turn_right()
        move()
    else:
        turn_left()'''