#intermediate - Files, Directories and Paths
#adding high_score to day 20

file = open("my_file.txt")
content = file.read()
print(content)
file.close()

with open("my_file.txt") as file:
    content = file.read()
    print(content)
#with open("my_file.txt", mode="w", ) as file:
#    #overwrite everything
#    file.write("New text.")
with open("my_file.txt", mode="r", ) as file:
    #read
    content = file.read()
    print(content)
with open("my_file.txt", mode="a", ) as file:
    #appending
    file.write("\nMy name is Julia.")
with open("my_file.txt", mode="r", ) as file:
    #read
    content = file.read()
    print(content)
with open("new_file.txt", mode="w", ) as file:
    #new file that does not exit atm
    file.write("New text.")


with open(r'\Users\Mustermann\Desktop\test3.txt', mode="r") as file:
    #Absolute PATH
    #both possible
    #\Users\Mustermann\Desktop\test3.txt
    #C:\Users\Mustermann\Desktop\test3.txt
    content = file.read()
    print(content)
with open(r"../../../../Desktop/test3.txt", mode="r") as file:
    #Relative Path
    #C:\Users\Mustermann\PycharmProjects\100 Days of code - Python\Day 24 - Files, Directories, Paths\test3.txt
    #                                                           ..\..\..\Desktop\test3.txt
    content = file.read()
    print(content)