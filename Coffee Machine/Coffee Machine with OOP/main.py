from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def check_finished() -> bool:
    """
    Determines whether user wants to order another drink
    :return: True or False whether user wants another drink.
    """
    get_new_drink = input("Would you like another drink? type 'y' or 'n': ").lower()
    return get_new_drink == "n"


menu = Menu()
money = MoneyMachine()
coffee_machine = CoffeeMaker()

finished = False
while not finished:
    order_name = input(f"What would you like:\nType 'Espresso', 'Latte' or 'Cappuccino'\n").lower()

    if order_name == "off":
        exit()

    elif order_name == "report":
        coffee_machine.report()
        money.report()

    else:
        order = menu.find_drink(order_name)
        if order is not None and coffee_machine.is_resource_sufficient(order) and money.make_payment(order.cost):
            coffee_machine.make_coffee(order)

    finished = check_finished()
    if finished:
        print("Goodbye!")
