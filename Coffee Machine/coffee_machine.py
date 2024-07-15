from art import logo
from menu import MENU
from resources import RESOURCES as resources
from drink_mapping import DRINK_CHOICE as drink_choice
from currency_value import COINS_VALUE as coins_value


def check_resources(drink: str) -> list:
    """
    Checks if sufficient resources are present to fill the order.
    :param drink: The drink chosen by the user.
    :return: A list of missing resources.
    """
    missing_resources = []
    drink_resources = MENU.get(drink).get("ingredients")

    for x in drink_resources:
        if resources[x] < drink_resources[x]:
            missing_resources.append(x)
    return missing_resources


def print_inventory(inventory: dict) -> None:
    """
    Prints the inventory report.
    :param inventory: A dictionary with the ingredients and the amounts as key-value pairs.
    :return: None
    """
    print("Inventory: ")
    for item, amount in inventory.items():
        if item == "money":
            amount = '${:,.2f}'.format(amount)
        print("{}, {}".format(item, amount))


def process_coins(cost_of_drink: float) -> dict:
    """
    Logs the coins the user wants to pay with for their drink
    :param cost_of_drink: The cost of the drink ordered by the user
    :return: A dictionary of the coins the user wants to pay with
            containing the coin name and quantity as the key-value pair.
    """

    quantity_of_coins = {}
    quantity_of_coins["quarter"] = int(
        input(f"That will be {'${:,.2f}'.format(cost_of_drink)}, how would you like to pay?\nquarters: "))
    quantity_of_coins["dime"] = int(input("dimes: "))
    quantity_of_coins["nickle"] = int(input("nickles: "))
    quantity_of_coins["penny"] = int(input("pennies: "))
    return quantity_of_coins


def calculate_total_paid(quantity_of_coins: dict) -> float:
    """
    Calculates the total value of coins given by the user to purchase their drink.
    :param quantity_of_coins: A dictionary of coins the user wants to
           pay with containing the coin name and quantity as the key-value pairs.
    :return: The sum of the value of coins given by the user.
    """
    processing_coins = []
    for x in quantity_of_coins:
        multiply = quantity_of_coins[x] * coins_value[x]
        processing_coins.append(multiply)
    total_paid = sum(processing_coins)
    return total_paid


def check_transaction_valid(total_paid: float, cost_of_drink: float) -> bool:
    """
    Checks whether the transaction is successful
    :param total_paid: The sum of the value of coins given by the user.
    :param cost_of_drink: The cost of the drink ordered by the user
    :return: True or False for whether the transaction was successful or not.
    """
    return total_paid < cost_of_drink


def calculate_change(total_paid: float, cost_of_drink: float) -> float:
    """
    Calculates the change owed to the user.
    :param total_paid: The sum of the value of coins given by the user.
    :param cost_of_drink: The cost of the drink ordered by the user.
    :return: The amount of money owed to the user as a float type
    """
    if total_paid > cost_of_drink:
        change = total_paid - cost_of_drink
        return change


def make_coffee(drink: str, cost_of_drink: float) -> None:
    """
    Adjusts the inventory of the coffee machine as a result of the ordered being filled.
    :param drink: The drink chosen by the user.
    :param cost_of_drink: The cost of the drink ordered by the user.
    :return: None
    """
    drink_ingredients = MENU.get(drink).get("ingredients")
    for x in drink_ingredients:
        resources[x] -= drink_ingredients[x]
    resources["money"] += cost_of_drink


def check_finished() -> bool:
    """
    Determines whether user wants to order another drink
    :return: True or False whether user wants another drink.
    """
    get_new_drink = input("Would you like another drink? type 'y' or 'n': ").lower()
    return get_new_drink == "n"


def main():
    print(logo)
    finished = False
    while not finished:
        choice = input(
            "What would you like:\nType 'e' for Espresso\nType 'l' for Latte\nType 'c' for Cappuccino\n").lower()

        if choice in drink_choice.keys():
            drink = drink_choice[choice]
            cost_of_drink = MENU.get(drink).get("cost")
            resources_missing = check_resources(drink)
            if len(resources_missing) != 0:
                print(f"Sorry, there is not enough {' & '.join(resources_missing)}.")
                exit()
        elif choice == "report":
            print_inventory(resources)
            continue_order = input("Do you want to go back to order a drink? enter 'y' or 'n': ").lower()
            if continue_order == "n":
                exit()
            else:
                continue
        elif choice == "off":
            exit()
        else:
            print("invalid entry")
            continue

        num_of_coins = process_coins(cost_of_drink)
        money_paid = calculate_total_paid(num_of_coins)
        funds_insufficient = check_transaction_valid(money_paid, cost_of_drink)

        if funds_insufficient:
            print("Insufficient funds. Money refunded.")
            continue

        change_due = calculate_change(money_paid, cost_of_drink)
        if change_due > 0:
            change = '${:,.2f}'.format(change_due)
            print(f"Your change is: {change}")

        make_coffee(drink, cost_of_drink)
        print(f"Enjoy your {drink}!")

        finished = check_finished()
        if finished:
            print("Goodbye!")


if __name__ == "__main__":
    main()
