# Step 5
import random
import hangman_art
import hangman_words


# ############# variables ################
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
# ########################################

print(hangman_art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# ################# Main logic #################
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        print(f"You guessed {guess}, it's not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
# ############################################
