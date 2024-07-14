MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 300,
}

drink_choice = {
    "e": "espresso",
    "l": "latte",
    "c": "cappuccino",
}

coins_value = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01,
}

def check_resources(drink):
    missing_resources = []
    drink_resources = MENU.get(drink).get("ingredients")

    for x in drink_resources:
        if resources[x] < drink_resources[x]:
            missing_resources.append(x)
    return missing_resources


# def process_coins():


choice = input("What would you like:\nType 'e' for Espresso\nType 'l' for Latte\nType 'c' for Cappuccino\n").lower()

if choice == "off":
    exit()
elif choice == "report":
    print(resources)
elif choice in drink_choice.keys():
    drink = drink_choice[choice]
    resources_available = check_resources(drink)
    if len(resources_available) != 0:
        print(f"add {resources_available}")
        exit()


    cost_of_drink = MENU.get(drink).get("cost")
    quantity_of_coins = {}
    quantity_of_coins["quarter"] = int(input(f"That will be ${cost_of_drink}, how would you like to pay?\nquarters: "))
    quantity_of_coins["dime"] = int(input("dimes: "))
    quantity_of_coins["nickle"] = int(input("nickles: "))
    quantity_of_coins["penny"] = int(input("pennies: "))

    processing_coins = []
    for x in quantity_of_coins:
        multiply = quantity_of_coins[x] * coins_value[x]
        processing_coins.append(multiply)

    total_paid = sum(processing_coins)

# check if transaction valid

    if total_paid < cost_of_drink:
        print("Insufficient funds. Money refunded.")
        exit()
        
    if total_paid > cost_of_drink:
        change = total_paid - cost_of_drink
        change = '${:,.2f}'.format(change)
        print(f"Your change is: ${change}")

# make coffee
# subtract ingredients for drink from the resources


