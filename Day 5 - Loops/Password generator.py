import random, sys
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))
if (nr_numbers + nr_symbols) < nr_letters:
    nr_letters = nr_letters - (nr_numbers + nr_symbols)
else:
    sys.exit()
password = []
for i in range(0, nr_letters):
        password.append(random.choice(letters))
for i in range(0, nr_symbols):
        password.append(random.choice(special_chars))
for i in range(0, nr_numbers):
        password.append(random.choice(numbers))
random.shuffle(password)
'''print(*password, sep = "")'''
password_output = ""
for char in password:
    password_output += char

print(f"Your Password is: {password_output}")


