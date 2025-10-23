import time
from data import flavours, resources


def order(machine_resources):
    c_order = input("What would you like? Espresso / Latte / Cappuccino\n").lower()
    for key, value in flavours.items():
        if value["name"] == c_order:
            return brew_coffee(machine_resources, value)
    if c_order == "off":
        return offline(machine_resources)
    elif c_order == "report":
        return report(machine_resources)
    else:
        return print("Order not avaible, please try again."), time.sleep(2.5), order(machine_resources)


def offline(machine_resources):
    password = "milk"
    c_password = input("Machine is shutting down. Please insert password: ")
    if password == c_password:
        for i in range(10, 0, -1):  # startet bei 10, endet bei 1, Schritt -1
            print(f"{i}...")
            time.sleep(1)
        return None
    else:
        print("Wrong password")
        return order(machine_resources)


def report(machine_resources):
    password = "milk"
    c_password = input("Generating report. Please insert password: ")
    if password == c_password:
        for key, value in machine_resources.items():
            print(f"{key}: {value}")
        return order(machine_resources)
    else:
        print("Wrong password")
        return order(machine_resources)


def brew_coffee(machine_resources, value):
    for key, stock in value["ingredients"].items():
        for key2, stock2 in machine_resources.items():
            if key == key2:
                if stock > stock2:
                    return print(f"Order canceled, not enoguh {key} in the machine."), order(machine_resources)
                print(f"{key} is being prepared")
    machine_resources["money"] = payment(machine_resources, value)
    for key, stock in value["ingredients"].items():
        for key2, stock2 in machine_resources.items():
            if key == key2:
                new_stock = stock2 - stock
                machine_resources[key2] = new_stock
    c_order = value["name"]
    print(f"Your {c_order} is ready.")
    return order(machine_resources)


def payment(machine_resources, value):
    price = value["price"]
    print(f'Please insert coins. Price: {value["price"]}')
    c_quarter = input("Please insert quarters: ")
    c_dime = input("Please insert dimes: ")
    c_nickel = input("Please insert nickels: ")
    c_pennie = input("Please insert pennies: ")
    if c_quarter.isdigit() and c_dime.isdigit() and c_nickel.isdigit() and c_pennie.isdigit():
        c_quarter = int(c_quarter)
        c_dime = int(c_dime)
        c_nickel = int(c_nickel)
        c_pennie = int(c_pennie)
    else:
        return print("Please only insert Coins. Order canceled"), order(machine_resources)
    count = (c_quarter * 0.25) + (c_dime * 0.10) + (c_nickel * 0.05) + (c_pennie * 0.01)
    if count < value["price"]:
        return print("Not enough Money, order canceled"), order(machine_resources)
    else:
        count = round(count, 2)
        print(f"Quarter x {c_quarter} = €{c_quarter * 0.25}")
        print(f"Dime x {c_dime} = €{c_dime * 0.10}")
        print(f"Nickel x {c_nickel} = €{c_nickel * 0.05}")
        print(f"Quarter x {c_pennie} = €{c_pennie * 0.01}")
        print(f"Total €{count}")
        change = round(count, 2) - price
        print(f"Change: €{round(change, 2)}")
        count = round(count, 2) - change
        print("Money accepted")
        return count


order(resources)