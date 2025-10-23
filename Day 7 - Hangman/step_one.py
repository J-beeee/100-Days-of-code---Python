import random
word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
print(random_word)

#number_of_letters = len(random_word)
#print(number_of_letters)
#list_word = list(random_word)
#print(list_word)

guess = input("Guess a Letter: ").lower()
'''letter = 0
for letter in range(0, number_of_letters):
    if guess == list_word[letter]:
        print("right")
    else:
        print("wrong")
letter += 1'''

for letter in random_word:
    if guess == letter:
        print("right")
    else:
        print("wrong")