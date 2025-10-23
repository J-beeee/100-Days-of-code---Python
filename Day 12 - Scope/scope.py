#Global Scope
appel = 1
player_health = 10

print(f"Appels: {appel}")

def increase_appel1():
    """Local Scope"""
    appel = 2
    print(f"Appels: {appel} - {player_health}")

def increase_appel2():
    """Global Scope"""
    global appel
    appel += 1
    print(f"Appels: {appel} - {player_health}")

def increase_appel3(thing):
    thing += 1
    print(f"Appels: {thing} - {player_health}")

increase_appel3(appel)

# There is no Block Scope in Python!
game_lvl = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_lvl < 5:
        new_enemy = enemies[0]

    print(new_enemy)

PI = 3.14159
GOOGLE_URL = "https://www.google.com"

def my_function():
    print(GOOGLE_URL)
