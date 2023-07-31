from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "off":
        print("Goodbye!")
        machine_is_on = False
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    elif menu.find_drink(order) is not None:
        coffee = menu.find_drink(order)
        is_coffee_doable = coffee_machine.is_resource_sufficient(coffee)
        if is_coffee_doable:
            coins_are_sufficient = money_machine.make_payment(coffee.cost)
            if coins_are_sufficient:
                coffee_machine.make_coffee(coffee)
