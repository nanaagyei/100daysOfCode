from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
drink_maker = CoffeeMaker()
drink_menu = Menu()
# drink_menu_items = MenuItem()
money = MoneyMachine()

while is_machine_on:
    choice = input(f"What would you like for today? ({drink_menu.get_items()}): ")
    if choice.lower() == "off":
        is_machine_on = False
    elif choice.lower() == "report":
        drink_maker.report()
        money.report()
    else:
        drink = drink_menu.find_drink(choice.lower())
        if drink_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            drink_maker.make_coffee(drink)


