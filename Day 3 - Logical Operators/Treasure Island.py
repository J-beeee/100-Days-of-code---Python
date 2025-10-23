import time
home = '''
        )
       (  (              .^.
        \) )           .'.^.'.
         (/          .'.'---'.'.
        _\)_       .'.'-------'.'.
       (__)()    .'.'-,=======.-'.'.
       (_)__)  .'.'---|   |   |---'.'.
       (__)_),'.'-----|   |   |-----'.'.
       ()__.'.'-------|___|___|-------'.'.
       (_.'.'---------------------------'.'.
       .'.'-------------------------------'.'.
      """""|====..====.=======.====..====|"""""
       ()_)|    ||    |.-----.|    ||    |
       (_)_|    ||    ||     ||    ||    |
       (...|____||____||_____||____||____|
      (_)_(|----------| _____o|----------|
      (_)(_|----------||     ||----------|
      (__)(|----------||_____||----------|
      (_)(_|---------|"""""""""|---------|
      ()()(|--------|"""""""""""|--------|
Zot-wWUwwuw|wwWWwuu|"""""""""""""|uwuwuuW|wuwwuuwu
'''
print('''
                   _,,,_
                 .'     `'.
                /     ____ 
               |    .'_  _\/
               /    ) a  a|         .----.
              /    (    > |        /|     '--.
             (      ) ._  /        ||    ]|   `-.
             )    _/-.__.'`\       ||    ]|    ::|
            (  .-'`-.   \__ )      ||    ]|    ::|
             `/      `-./  `.      ||    ]|    ::|
            _ |    \      \  \     \|    ]|   .-'
           / \|     \   \  \  \     L.__  .--'(
          |   |\     `. /  /   \  ,---|_      \---------,
          |   `\.     '. /`\   \/ .--._|=-    |_      /|
          |     \ '.     '._ './`\/ .-'          '.   / |
          |     |   `'.     `;-:-;`)|             |-./  |
          |    /_      `'--./_  ` )/'-------------')/)  |
          \   | `""""----"`\//`""`/,===..'`````````/ (  |
           |  |            / `---` `==='          /   ) |
           /  \           /                      /   (  |
          |    '------.  |'--------------------'|     ) |
           \           `-|                      |    /  |
            `--...,______|                      |   (   |
                   | |   |                      |    ) ,|
                   | |   |                      |   ( /||
                   | |   |                      |   )/ `"
                  /   \  |                      |  (/
            jgs .' /I\ '.|                      |  /)
             .-'_.'/ \. |                      | /
             ```  `"""` `| .-------------------.||
                         `"`                   `"`
''')
time.sleep(3)
print('''



















''')
print("Welcome to your mission to Escape from work.")
print("Your mission to escape from work with as fast as possible")
print("You are sitting in your office, its 11:50am.")
time = 1150
aura_status = False
aura = "100"
decision_one = input("What are u doing? You going to wait until all at lunch or you try to get home while they prepare there lunch?\n  Wait or Go?: ").lower()
if decision_one == "wait":
    print("All of your colleagues are at lunch u can easy get at of the House.")
    decision_one = True
    time += 10
elif decision_one == "go":
    print("Your colleagues catch you the corridor, you have to stay until 1pm.")
    print("After the lunch you going to leave the house.")
    decision_one = False
    time += 150
else:
    print("what???")
    raise SystemExit
decision_two = input("You are in front of workplace, you see your boss is coming from a meeting.\nWhat are u going to do? Just pass her or hide under some cars in front of your workspace?\nPass or Hide?: ").lower()
if decision_one == True and decision_two == "pass":
    print("At 11:50 a.m., as you try to slip past your boss on your way home, she gets furious and piles a mountain of new tasks on you — enough to keep you busy for another three hours.")
    decision_two = False
    time += 300
elif decision_one == True and decision_two == "hide":
    print("You hide like a weasel under the car. Your boss doesn’t notice you, but a few colleagues spot you from the window — and your aura takes a drastic hit.")
    decision_two = True
    aura = "-10"
    aura_status = True
elif decision_one == False and decision_two == "pass":
    print("Your boss wishes you a nice evening")
    decision_two = True
elif decision_one == False and decision_two == "hide":
    print("You hide behind one of the cars in the parking lot — unfortunately, it’s your boss’s car. She catches you and lectures you for 30 minutes about your faulty behavior.")
    decision_two = False
    time += 50
decision_three = input("You finally arrive the bus station but there are three buses they all drive to your destination... Home. But witch u wanna take?\n Pink, Blue or Green?: ").lower()
if decision_one == True and decision_two == True and decision_three == "pink":
    print("You catch the pink bus and get home in no time. On top of that, your boss calls you on the way and tells you that you can take the next five days off with pay.")
    time += 50
    print(f"Time: {time}pm")
    if aura_status:
        print("Aura level: " + aura)
    print("Congratulations, you’re home.")
    print(home)
elif decision_three == "pink":
    print("You catch the pink bus and get home in no time. On top of that, your boss calls you on the way and tells you that you can take the next five days off with pay.")
    time += 50
    print(f"Time: {time}pm")
    if aura_status:
        print("Aura level: " + aura)
    print("Congratulations, you’re home — and in just a few hours, it’s time to head back to work.")
    print(home)
elif decision_three == "blue":
    print("The bus goes through over a hundred villages, and you don’t get home until three hours later.")
    time += 300
    print(f"Time: {time}pm")
    if aura_status:
        print("Aura level: " + aura)
    print("Congratulations, you’re home — and in just a few hours, it’s time to head back to work.")
    print(home)
else:
    print("The bus driver takes a wrong turn, and you get home with a slight delay.")
    time += 100
    print(f"Time: {time}pm")
    if aura_status:
        print("Aura level: " + aura)
    print("Congratulations, you’re home — and in just a few hours, it’s time to head back to work.")
    print(home)

