students_score = [87, 45, 92, 76, 59, 100, 34, 68, 82, 71,
                  53, 96, 41, 89, 63, 78, 25, 84, 99, 60]
sum_score = sum(students_score)
print(sum_score)
sum_score2 = 0
for n in students_score:
    sum_score2 += n
print(sum_score2)

max_score = max(students_score)
print(max_score)
compare = 0
for i in students_score:
    if i > compare:
        compare =  i
print(compare)
