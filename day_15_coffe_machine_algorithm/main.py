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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins(cost):
    coins = {
        'quarters': '0.25',
        'dimes': '0.1',
        'nickles': '0.05',
        'pennies': '0.01'
    }
    coim_sum = 0
    for coin in coins:
        coin_count = int(input(f"How many {coin}?: "))
        coim_sum += float(coins[coin]) * coin_count
    if cost > coim_sum:
        print("Sorry that's not enough money. Money refunded.\n")
        return False
    elif cost == coim_sum:
        print("Thanks for you buy!\n")
    else:
        change = "{:.2f}".format(coim_sum - cost)
        print(f"\nHere is {change} in change.")
    return True


def resource_check(resources, order):
    for ingredient in order:
        position = str(ingredient)
        if not resources[position] >= order[position]:
            return position
    return True


def report(earnings, status):
    elements = ['water', 'milk', 'coffee', 'money']
    for element in elements:
        if element == "money":
            print(f"Money: ${earnings}")
        elif element in ['water', 'milk']:
            print(f"{element}: {status[element]}ml")
        else:
            print(f'{element}: {status[element]}g')


def coffe_machine():
    current_resources = RESOURCES
    money = 0

    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        end_input = f"Here is your {user_input} ☕ Enjoy!"

        if user_input in ['espresso', 'latte', 'capuccino']:

            user_input = MENU[user_input]
            order_ingredient = user_input['ingredients']
            result = resource_check(current_resources, order_ingredient)

            if result is True:
                product_cost = float(user_input['cost'])
                print(f"\nThat would be {product_cost}")
                print("Please insert coins")

                if not process_coins(product_cost):
                    coffe_machine()
                else:

                    money += product_cost
                    elements = ['water', 'milk', 'coffee']
                    for element in elements:
                        if element in order_ingredient:
                            current_resources[element] -= int(order_ingredient[element])
                    print(end_input)
            else:
                print(f"Sorry there is not enough {result}.")
        elif user_input in ['off', 'report']:
            if user_input == 'off':
                return
            else:
                report(money, current_resources)


if __name__ == "__main__":
    coffe_machine()
