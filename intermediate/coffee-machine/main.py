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
    "money": 0,
}


def make_an_order():
    input_is_invalid = True
    while input_is_invalid:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino" or coffee_type == "off" or coffee_type == "report":
            return coffee_type


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(coffee):
    if coffee == "espresso":
        if resources["water"] < MENU[coffee]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

    else:
        if resources["water"] < MENU[coffee]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        elif resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True


def process_coins():
    print("Please insert coins!")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    change = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return change


def check_inserted_money(money, coffee_type):
    if money >= MENU[coffee_type]["cost"]:
        resources["money"] += MENU[coffee_type]["cost"]
        change = money - MENU[coffee_type]["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type != "espresso":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    print(f"Here is your {coffee_type}. Enjoy!")


def coffee_machine():
    machine_is_on = True
    while machine_is_on:
        order = make_an_order()
        if order == "off":
            print("Goodbye!")
            machine_is_on = False
        elif order == "report":
            print_report()
        else:
            is_coffee_doable = check_resources(order)
            if is_coffee_doable:
                inserted_money = process_coins()
                enough_money_inserted = (check_inserted_money(inserted_money, order))
                if enough_money_inserted:
                    make_coffee(order)


coffee_machine()
