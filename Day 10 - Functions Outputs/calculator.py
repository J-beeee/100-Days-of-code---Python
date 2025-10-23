def calculator_start():
    f_number = float(input("What's the first number?:\n"))
    return operator_n_number(first_number= f_number)
def operator_n_number(first_number):
    operator = input("Pick an operation:\n+\n-\n*\n/\n")
    n_number = float(input("Which is your next number?:\n"))
    return result(first_number=first_number, operator=operator, second_number=n_number)
def result(first_number, operator, second_number):
    if operator == "+":
        calculation_result = first_number + second_number
    elif operator == "-":
        calculation_result = first_number - second_number
    elif operator == "*":
        calculation_result = first_number * second_number
    elif operator == "/":
        calculation_result = first_number / second_number
    else:
        print("bug_result")
        calculation_result = 0
    print(f"{first_number} {operator} {second_number} = {calculation_result}")
    repeat = input(f"Type 'y' for continue calculating, type 'n' for start new calculation.;\n")
    if repeat == "y":
        return operator_n_number(first_number=calculation_result)
    elif repeat == "n":
        return calculator_start()
    return None

calculator_start()
