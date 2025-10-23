import random

word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
print(random_word)
guess_list = []
lives = 6

for letter in random_word:
    guess_list.append("_")

first_output = "".join(guess_list)
print(first_output)

while lives > 0 and ("_" in guess_list):
    guess = input("Guess a Letter: ").lower()
    count = 0
    if guess in random_word:
        for letter in random_word:
            if guess == letter:
                guess_list[count] = letter
            else:
                None
            count += 1
    else:
        lives -= 1
        print(f"Your lives {lives}")
    output = "".join(guess_list)
    print(output)
if lives == 0:
    print("You lost!")
elif "_" not in guess_list:
    print("You Won!")



