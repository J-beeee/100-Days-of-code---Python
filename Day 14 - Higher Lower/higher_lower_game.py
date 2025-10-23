import random
import art
import game_data


def game_ini():
    picked_persons = []
    print(art.logo)
    points = 0
    for _ in range(2):
        random_person(picked_persons)
    print(picked_persons)
    while picked_persons[-1]["name"] == picked_persons[-2]["name"]:
        del picked_persons[-1]
        random_person(picked_persons)
    person_output(points, picked_persons)

def person_output(points, picked_persons):
    print(f"\033[95mCompare Person A: {picked_persons[-2]["name"]}\033[0m")
    print(art.vs)
    print(f"\033[32mAgainst Person B: {picked_persons[-1]["name"]}\033[0m")
    guess = input("Who has more subscriptions? Type 'A' oder 'B': ").lower()
    print("\n"*5)
    compare(picked_persons, guess, points)

def random_person(picked_persons):
    picked_persons.append(random.choice(game_data.data))
    return picked_persons

def compare(list_picked, guess, points):
    a = list_picked[-2]["abos"]
    b = list_picked[-1]["abos"]
    #alternativ if a > b / b> A
    #return guess == True
    #damit kann man eine variable nutzen die wenn a>b und dein guess a dann True sonst False
    if guess == "a" and a >= b:
        points += 1
        print("\n"*20)
        print(f"\033[34mYou are right.\n{list_picked[-2]["name"]} - {a}\n{list_picked[-1]["name"]} - {b}\nYour Points: {points}\033[0m")
        if len(list_picked) == len(game_data.data):
            return print(f"\033[You are done!\033[0m")
        random_person(list_picked)
        while list_picked.count(list_picked[-1]) > 1:
            del list_picked[-1]
            random_person(list_picked)
        return person_output(points,list_picked)
    elif guess == "b" and b >=a:
        points += 1
        print("\n" * 20)
        print(f"\033[34mYou are right.\n{list_picked[-2]["name"]} - {a}\n{list_picked[-1]["name"]} - {b}\nYour Points: {points}\033[0m")
        if len(list_picked) == len(game_data.data):
            return print(f"\033[You are done!\033[0m")
        random_person(list_picked)
        while list_picked.count(list_picked[-1]) > 1:
            del list_picked[-1]
            random_person(list_picked)
        return person_output(points,list_picked)
    else:
        print("\n" * 20)
        print("\033[31mThat's wrong!\033[0m")
        return restart()

def restart():
    user_input = input("\033[31mYou wanna restart the game, type 'yes', 'no': \033[0m")
    print("\n" * 10)
    if user_input == "yes":
        return game_ini()
    else:
        return print("Have a nice day.")

game_ini()
