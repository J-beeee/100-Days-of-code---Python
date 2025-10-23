from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

while True:
    order = Menu()
    work = CoffeeMaker()
    cash = MoneyMachine()
    c_order = input(f"Chose a drink {order.get_items()}: ")
    print(c_order)
    if c_order == "report":
        work.report()
    c_order_m = (order.find_drink(c_order))
    var = c_order_m.cost
    if c_order_m is not None:
        if work.is_resource_sufficient(c_order_m):
            print(c_order)
            if cash.make_payment(var):
                work.make_coffee(c_order_m)
        else:
            print("Not enough ingredients")


