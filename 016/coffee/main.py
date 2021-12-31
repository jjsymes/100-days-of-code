from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        user_input = ""
        user_input = get_user_input(f"What would you like? ({menu.get_items()}): ", str)
        if user_input == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_input == "refill":
            print("To be implemented...")
        elif user_input == "profit":
            money_machine.report()
        elif user_input == "off":
            print("Turning machine off.")
            break
        else:
            item = menu.find_drink(user_input)
            if item and coffee_maker.is_resource_sufficient(item):
                payment_received = money_machine.make_payment(item.cost)
                if payment_received:
                    coffee_maker.make_coffee(item)


main()