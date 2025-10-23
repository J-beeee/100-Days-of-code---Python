import random
friends = ["Julia", "Fish", "Qwerty", "Lars", "Ivy", "Papa"]
family = ["Ivy", "Enrico", "Papa"]
humans = [friends, family]
random_int = random.randint(0, 5)
print(friends[random_int])
print(random.choice(friends))
print(len(friends))
print(humans[0][0])