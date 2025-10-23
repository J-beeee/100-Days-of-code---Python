import random
from hangman_art import hangman, stages_of_hangman
from hangman_words import word_list

print(hangman)

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
        print(f"********************You all ready tried the letter {guess}, try another.********************")
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
            print(f"******************** THE LETTER YOU CHOSE IS NOT IN THE WORD ********************")
            print(f"***************************** {lives}/6 LIVES LEFT *****************************")
        output = "".join(guess_list)
        print(f"**************************   {output}   **************************")
if lives == 0:
    print("********************YOU LOSE********************")
    print(f"********************THE WORD IS {random_word}********************")
elif "_" not in guess_list:
    print("********************You Won!********************")



