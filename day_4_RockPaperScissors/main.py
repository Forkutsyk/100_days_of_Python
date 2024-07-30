from random import randint
from os import system

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ART = [rock, paper, scissors]

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock 1 for Paper or 2 for Scissors\n"))
    computer_choice = randint(0, 2)

    if user_choice in [0, 1, 2]:
        print(ART[user_choice])
        print(f"Computer chose:\n{ART[computer_choice]}")
        if user_choice == 0 and computer_choice == 2:
            print("You win")
        elif user_choice == 1 and computer_choice == 0:
            print("You win")
        elif user_choice == 2 and computer_choice == 1:
            print("You win")
        else:
            print("You lose")
        user_choice2 = input("\nWould you like to play again? Type y or n : ").lower()
        if user_choice2 == 'y':
            system('cls')
        else:
            break
    else:
        system('cls')
        print("You have entered not valid number please try again.\n")
