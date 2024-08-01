import random
import os
from art import logo


def generate_cards(count):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return [random.choice(cards) for _ in range(count)]


def ace_checker(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1


def calculate_score(hand):
    ace_checker(hand)
    return sum(hand)


def player_move(player_hand, computer_hand):
    if calculate_score(player_hand) == 21 and calculate_score(computer_hand) == 21:
        print("It's a draw. You both have blackjack!")
        return True
    elif calculate_score(player_hand) == 21:
        print("You win. You have blackjack!")
        return True
    elif calculate_score(computer_hand) == 21:
        print("You lose. Opponent has blackjack!")
        return True

    while True:
        print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")

        if calculate_score(player_hand) > 21:
            break

        take_card_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if take_card_choice == 'n':
            break
        elif take_card_choice == 'y':
            player_hand.extend(generate_cards(1))

    return False


def computer_move(computer_hand):
    while calculate_score(computer_hand) < 17:
        computer_hand.extend(generate_cards(1))
        ace_checker(computer_hand)


def validation_check(user_input):
    possible_choice = ['y', 'n']
    if user_input not in possible_choice:
        print("You have entered not valid value please try again.")
        return False
    return True


def play_again_check():
    user_choice = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    valid_input = validation_check(user_choice)
    if valid_input is True:
        if user_choice == 'n':
            return True
        elif user_choice == 'y':
            os.system('clear')
            print(logo)
    else:
        play_again_check()


def main_logic():
    end_game = False
    print(logo)
    while not end_game:
        player_hand = generate_cards(2)
        computer_hand = generate_cards(2)

        end_game = player_move(player_hand, computer_hand)

        if not end_game:
            computer_move(computer_hand)

        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        if player_score > 21:
            print("You went over. Computer wins!")
        elif computer_score > 21:
            print("Opponent went over. You win!")
        elif player_score == computer_score:
            print("It's a draw!")
        elif player_score > computer_score:
            print("You win!")
        else:
            print("You lose!")

        end_game = play_again_check()


if __name__ == "__main__":
    main_logic()
