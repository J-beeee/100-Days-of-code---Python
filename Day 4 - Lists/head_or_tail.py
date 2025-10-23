import random

random_int = random.random()
if random_int <= 0.5:
    print("Head")
    print(random_int)
elif random_int > 0.5:
    print("Tail")
    print(random_int)

random_head_or_tail = random.randint(0, 1)
if random_head_or_tail == 0:
    print("Head")
else:
    print("Tail")