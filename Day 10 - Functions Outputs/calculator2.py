def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return  n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
          "-": subtract,
          "*": multiply,
          "/": divide,
          }
def calculator_start():
    n1 = float(input("What's the first number?:\n"))
    return operator_n_number(first_number= n1)
def operator_n_number(first_number):
    operator = input("Pick an operation:\n+\n-\n*\n/\n")
    while operator not in operations:
        print("Pick an operation:\n+\n-\n*\n/\n")
        return operator_n_number(first_number)
    n2 = float(input("Which is your next number?:\n"))
    return result(first_number=first_number, operator=operator, second_number=n2)
def result(first_number, operator, second_number):
    result = operations[operator](first_number, second_number)
    print(f"{first_number} {operator} {second_number} = {result}")
    repeat = input(f"Type 'y' for continue calculating, type 'n' for start new calculation.;\n")
    if repeat == "y":
        return operator_n_number(first_number=result)
    elif repeat == "n":
        return calculator_start()
    return None


calculator_start()
