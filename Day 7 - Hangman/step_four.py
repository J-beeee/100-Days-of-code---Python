import random
import os

hangman = ('''                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')
print(hangman)
stages_of_hangman = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
guess_list = []
lives = 6
stage = 0
for letter in random_word:
    guess_list.append("_")

first_output = "".join(guess_list)
print(first_output)
used_letters = []

while lives > 0 and ("_" in guess_list):
    guess = input("Guess a Letter: ").lower()
    count = 0
    if guess in used_letters:
        print(f"You all ready tried the letter {guess}, try another.")
    else:
        if guess in random_word:
            print(stages_of_hangman[stage])
            for letter in random_word:
                if guess == letter:
                    guess_list[count] = letter
                    used_letters.append(guess)
                else:
                    used_letters.append(guess)
                count += 1
        else:
            lives -= 1
            stage += 1
            print(stages_of_hangman[stage])
            print(f"Your lives {lives}")
        output = "".join(guess_list)
        print(output)
if lives == 0:
    print("You lost!")
elif "_" not in guess_list:
    print("You Won!")



