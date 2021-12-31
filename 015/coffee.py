import os

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

COINS = {
    "penny": {
        "value": 0.01
    },
    "nickel": {
        "value": 0.05
    },
    "dime": {
        "value": 0.1
    },
    "quarter": {
        "value": 0.25
    }
}

def report():
    global resources, money
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money: ${money}")

def insert_coins():
    print("Please insert coins.")
    quarters = get_user_input("How many quarters?: ", float)
    dimes = get_user_input("How many dimes?: ", float)
    nickels = get_user_input("How many nickels?: ", float)
    pennies = get_user_input("How many pennies?: ", float)
    balance = quarters * COINS["quarter"]["value"] + dimes * COINS["dime"]["value"] + nickels * COINS["nickel"]["value"] + pennies * COINS["penny"]["value"]
    print(f"Your balance is ${balance}")
    return balance

def order(item):
    global money, resources
    balance = 0.0
    balance += insert_coins()
    balance = round(balance, ndigits=2)
    if balance < MENU[item]["cost"]:
        print(f"Sorry, that's not enough money. Money refunded.")
    else:
        change = round(balance - MENU[item]["cost"], ndigits=2)
        ingredients = list(MENU[item]["ingredients"].keys())
        for ingredient in ingredients:
            resources[ingredient] -= MENU[item]["ingredients"][ingredient]
        print(f"Here is ${'{:.2f}'.format(change)} in change.")
        print(f"Here is your {item} ☕... Enjoy!")
        money += MENU[item]["cost"]
    money = round(money, ndigits=2)

def is_in_stock(item):
    global resources
    is_in_stock = True
    ingredients = list(MENU[item]["ingredients"].keys())
    for ingredient in ingredients:
        if MENU[item]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            is_in_stock = False
    return is_in_stock

def get_user_choice(input_prompt: str, valid_choices: list[str]):
    valid_input = False
    while not valid_input:
        user_input = input(input_prompt).lower()
        if user_input in valid_choices:
            valid_input = True
        else:
            pass
    return user_input

def get_user_input(input_prompt: str, type=float):
    valid_input = False
    while not valid_input:
        try:
            user_input = input(input_prompt)
            if type == float:
                user_input = float(user_input)
            elif type == int:
                user_input = int(user_input)
            else:
                pass
            valid_input = True
        except ValueError:
            print("Not a valid number!")
            pass
    return user_input

def refill():
    global resources
    resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

def withdraw():
    global money, admin_password
    user_input = get_user_input("Please enter the admin password: ", type=str)
    if user_input == admin_password:
        print(f"Here is ${money}")
        money = 0.0
    else:
        print("Incorrect password.")


choices = list(MENU.keys())
commands = ["report", "refill", "withdraw", "off"]
command = None
choice = None
money = 0.0
admin_password = os.getenv(key="ADMIN_PASSWORD", default="Pa55w0rd")
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


def main():
    while True:
        command = ""
        choice = ""
        user_input = get_user_choice(f"What would you like? ({'/'.join(choices)}): ", choices + commands)
        if user_input in choices:
            choice = user_input
        elif user_input in commands:
            command = user_input

        if command == "report":
            report()
        elif command == "refill":
            refill()
        elif command == "withdraw":
            withdraw()
        elif command == "off":
            print("Turning machine off.")
            break

        if choice and is_in_stock(choice):
            order(choice)


main()