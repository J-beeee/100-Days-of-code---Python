#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
import pandas
names = ["Alex", "Beth", "Dave", "Julia", "Ivy", "Wolfgang", "Freddie", "Eleanor"]

students_score ={students: random.randint(1,100) for students in names}
print(students_score)
pass_students = {students:score for (students,score) in students_score.items() if score > 70}
print(pass_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {item:len(item) for item in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {key:(value * 9/5) + 32 for (key,value) in weather_c.items()}
print(weather_f)
student_dict = {
    "student": ["julia", "Ivy", "Wolfgang"],
    "score": [56, 76, 100]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)
for (index, row) in student_df.iterrows():
    print(row)

