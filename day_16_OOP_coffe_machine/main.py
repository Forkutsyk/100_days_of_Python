from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system


def main_logic():
    olek_coffe_machine = Menu()
    current_resources = CoffeeMaker()
    terminal = MoneyMachine()
    valid_input = ['latte', 'espresso', 'cappuccino', 'off', 'report']

    while True:
        user_input = input(f"What would you like? ({olek_coffe_machine.get_items()}): ").lower()
        if user_input not in valid_input:
            system('cls')
            print("Sorry there is some connection problem. Please choose again.\n")
        else:
            if user_input == "off":
                return
            elif user_input == "report":
                current_resources.report()
                terminal.report()
            else:           
                chosen_product = olek_coffe_machine.find_drink(user_input)
                resource_check_true = current_resources.is_resource_sufficient(chosen_product)
            
                if resource_check_true:
                    terminal.make_payment(chosen_product.cost)
                    current_resources.make_coffee(chosen_product)


main_logic()
