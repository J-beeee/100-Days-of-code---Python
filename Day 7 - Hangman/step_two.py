import random
word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
print(random_word)
placeholder = ""
word_length = len(random_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
guess = input("Guess a Letter: ").lower()
display = ""

for letter in random_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)



guess_list = []
for letter in random_word:
    guess_list.append("_")
count = 0
for letter in random_word:
    if guess == letter:
        guess_list.remove("_")
        guess_list.insert(count, guess)
    else:
        None
    count +=1
output = "".join(guess_list)
print(output)