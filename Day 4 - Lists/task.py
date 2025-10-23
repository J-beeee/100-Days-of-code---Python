import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.my_favourite_number)

#never include 1 or in this 100
random_number_0_to_1 = random.random() * 100
print(random_number_0_to_1)

#include 100
random_float = random.uniform(1, 10) *10
print(random_float)