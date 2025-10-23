from tkinter import Frame

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you easily call over and over again.",
    "loop": "The action of doing something over and over again.",
}

print(programming_dictionary)
programming_dictionary["Julia"] = "Text 4"
print(programming_dictionary)
empty_dictionary = {}

programming_dictionary = {}
print(programming_dictionary)
programming_dictionary["Julia"] = "Name of a Person."

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for person in student_scores:
    if student_scores[person] >= 91:
        student_grades[person] = "Outstanding"
    elif student_scores[person] >= 81:
        student_grades[person] = "Exceeds Expectations"
    elif student_scores[person] >= 71:
        student_grades[person] = "Acceptable"
    elif student_scores[person] <= 70:
        student_grades[person] = "Fail"
print(student_grades)

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "num_times_visited": 8,
    },
}

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
print(travel_log["Germany"]["cities_visited"][2])