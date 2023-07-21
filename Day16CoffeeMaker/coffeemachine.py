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
    "coffee": 100,
}

profit = 0


def process_coins():
    """
    Processes all coins and converts them to dollars
    :return: The sum of all coins
    """
    print("Please insert coins")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.1
    total += float(input("How many nickles?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total


def is_resource_sufficient(order_ingredients):
    """
    Determines whether order can be made based on available resources.
    :param order_ingredients: A dictionary containing the ingredients for the order
    :return: True if resource is sufficient, False if otherwise
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, we do not have enough {item}")
            return False
        else:
            return True


def is_transaction_successful(money_received, drink_cost):
    """
    Determines if money received is up to cost of drink
    :param money_received: float - money received by user
    :param drink_cost: float - cost of drink
    :return: True if money received is greater than or equal to drink cost, False if otherwise
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Not enough money for drink. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Make drink/coffee with ingredients. Deducts each ingredient from resource
    :param drink_name: str: name of drink
    :param order_ingredients: dict: a dictionary containing the ingredients for the drink
    :return: None
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} . Enjoy!")


machine_is_on = True

while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "off":
        machine_is_on = False
    elif choice.lower() == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice.lower()]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

