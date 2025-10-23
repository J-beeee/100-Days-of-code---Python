#start_point = [new_item for item in list if test]

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)
name = "Julia"
new_list = [letter for letter in name]
print(new_list)

double_num = [num*2 for num in range(1, 5)]
print(double_num)


names = ["Alex", "Beth", "Dave", "Julia", "Ivy", "Wolfgang", "Freddie", "Eleanor"]

short_names = [name for name in names if len(name)<=4]
print(short_names)
long_names_upper = [name.upper() for name in names if len(name) >=5]
print(long_names_upper)
long_names_upper = [name[-1::-1].lower() for name in names if len(name) >=5]
print(long_names_upper)