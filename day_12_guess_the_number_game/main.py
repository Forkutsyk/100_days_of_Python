from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(answer, player_guess, tries):
    """Check the player's guess against the answer and return the remaining tries."""
    if player_guess == answer:
        print(f"You got it! The answer was {answer}")

    elif player_guess > answer:
        print("Too high!")
        return tries - 1

    elif player_guess < answer:
        print("Too low!")
        return tries - 1


def difficulty_choice():
    """Asks the user to select difficulty and validate the answer. Return the number of tries(int)"""
    while True:
        try:
            game_difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ").strip().lower()
            if game_difficulty not in ['easy', 'hard']:
                raise ValueError("Invalid game difficulty. Please enter 'easy' or 'hard'.")

            return EASY_LEVEL_TURNS if game_difficulty == 'easy' else HARD_LEVEL_TURNS

        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guessed_int = random.randint(1, 100)
    print(f"Psst the answer is {guessed_int}")

    number_of_tries = difficulty_choice()
    while True:
        print(f"\nYou have {number_of_tries} attempts remaining to guess the number")
        player_guess = input("Make guess: ")

        if player_guess.isdigit() and not int(player_guess) > 100:
            player_guess = int(player_guess)
            number_of_tries = check_answer(guessed_int, player_guess, number_of_tries)
            if number_of_tries == 0:
                print("You've run out of guesses, you lose")
                return

        else:
            print("There is something wrong in your input. Please guess again")


if __name__ == "__main__":
    game()
