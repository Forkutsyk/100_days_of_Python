from art import logo, vs
from game_data import data
import os
import random


def get_higher_follower_count(option_a, option_b):
    if option_a['follower_count'] > option_b['follower_count']:
        return option_a
    else:
        return option_b


def game_output(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."


def game():
    print(logo)
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    score = 0
    result = 0

    if score > 0:
        print(f"You're right! Current score: {score}.")

    while True:
        compare_a = compare_b
        compare_b = random.choice(data)

        while compare_a == compare_b:
            compare_b = random.choice(data)

        print(f"Compare A: {game_output(compare_a)}")
        print(vs)
        print(f"Against B: {game_output(compare_b)}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_choice in ['a', 'b']:
            user_choice = compare_a if user_choice == 'a' else compare_b
            remaining_option = compare_a if user_choice != compare_a else compare_b
            result = get_higher_follower_count(user_choice, remaining_option)
            os.system('cls')
            print(logo)

            if result == user_choice:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry that's wrong. Final score: {score}")
                return
        else:
            os.system('cls')
            print(logo)
            print("\nThere is something wrong with your input. Please enter 'A' or 'B'\n")


if __name__ == "__main__":
    game()
