from menu import menu,menuitem
from coffee_maker import coffeemaker
from money_machine import moneymachine


money_machine = moneymachine()
coffee_maker = coffeemaker()
menu = menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resources_sufficient(drink):
           coffee_maker.make_coffee(drink)