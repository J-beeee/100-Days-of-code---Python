import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
try:
    human = int(input("What du you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
except ValueError:
    human = None
if human == 0:
    print(rock)
    print("Your choice is rock.")
elif human == 1:
    print(paper)
    print("Your choice is paper.")
elif human == 2:
    print(scissors)
    print("Your choice is scissors.")
else:
    print("You lost, try again!")
    sys.exit()

options = [0, 1, 2]
not_human = random.choice(options)
if not_human == 0:
    print(rock)
    print("The PC choice is rock.")
elif not_human == 1:
    print(paper)
    print("The PC choice is paper.")
else:
    print(scissors)
    print("The PC choice is scissors.")

if human == 2 and not_human == 0:
    print("You lost, try again!")
elif not_human == 2 and human == 0:
    print("You won!")
elif not_human > human:
    print("You lost, try again!")
elif human > not_human:
    print("You won!")
else:
    print("draw")
