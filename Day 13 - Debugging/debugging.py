#first programmer = Grace Hopper
#Tip 1 - describe the bug
#tip 2 - try to reproduce the bug
try:
    age = int(input("How old are you?"))
except ValueError:
    age = ""
    print("You have typed in an an invalid number. Please try again with numerical response such as 15.")

if age > 18:
    print(f"You can drive at age {age}")

#Tip 3 - print is your friend.
#Tip 4 - Use a debugger
python_tutor = "https://www.pythontutor.com"
thonny = "thonny editor"
#Pycharm debugger - red dot - breakpoint
#Tip 5 stackoverflow