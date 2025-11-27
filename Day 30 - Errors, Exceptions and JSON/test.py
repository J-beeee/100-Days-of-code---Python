#----------------------test----------------------#
height = float(input("Height: "))
weight = float(input("Weight: "))

if height >= 3:
    raise ValueError("Height over 3 Meter.")

bmi = weight / height ** 2
print(bmi)


#----------------------FileNotFoundError----------------------#
try:
    with open("a_file.txt") as file:
        file.read()
    file = open("a_file.txt")
except FileNotFoundError:
    with open("a_file.txt", mode="w") as file:
        file.write("Data created")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    raise KeyError("This is a test error")
#----------------------KeyError----------------------#
#try:
#    a_dictionary = {
#        "key": "value"
#    }
#    value = a_dictionary["non_existent_key"]
#except KeyError as error_message:
#    print(f"Key : {error_message} does not exist")

#----------------------IndexError----------------------#
#fruit_list = [0,1,2]
#fruit = fruit_list[3]
#----------------------TypeError----------------------#
#text = "abc"
#print(text + 5)