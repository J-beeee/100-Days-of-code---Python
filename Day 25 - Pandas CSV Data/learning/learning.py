with open("weather_data.csv", mode="r") as data_file:
    data = data_file.readlines()
    print(data)
#
#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.DictReader(data_file)
#    temperatures = []
#    for row in data:
#        temperatures.append(int(row["temp"]))
#    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list[1])
#average_temp = sum(temp_list)/len(temp_list)
#print(round(average_temp,1))
##print(f"{sum(temp_list)/len(temp_list):.2f}")
##print(type((f"{sum(temp_list)/len(temp_list):.2f}")))
print(data["temp"].mean())
print(data["temp"].max())

print(data["day"].max())
#start_list = data["day"]
#alphabetic_list = []
#print(start_list)
#for _ in range(len(start_list)):
#    n = start_list.max()
#    alphabetic_list.append(n)
#    start_list= start_list.drop(index=start_list.idxmax())
#
#
#print(alphabetic_list)
#x = data["day"].sort_values().to_list()
#print(x)
#
#y = data.condition
#print(y)
#
#print(data[data.condition == data.temp.max()])
#
#monday = data[data.day == "Monday"]
#print((monday.temp* 9/5) + 32)
#
#data_dict = {
#    "students": ["Amy", "James", "Julia"],
#    "scores":   [76, 56, 65]
#}
#
#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("new_data.csv")