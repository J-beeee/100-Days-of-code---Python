def greet(name):
    print(f"It's to early, {name}.")
    print("I could sleep longer, but i couldn't.")
    print("Good Morning.")

greet("julia")

def greet_with(name, location):
    print(f"Hello {name}, i know u live in {location}.")

greet_with("Kai", "berlin")
greet_with(location = "Berlin", name = "kai")
