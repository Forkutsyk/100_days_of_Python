import random


def password_generator(letter_count, symbols_count, number_count):
    # Define the characters to use in the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate the required number of each type of character
    elements = []
    elements += [random.choice(letters) for _ in range(letter_count)]
    elements += [random.choice(numbers) for _ in range(symbols_count)]
    elements += [random.choice(symbols) for _ in range(number_count)]

    # Shuffle the list to ensure the characters are mixed
    random.shuffle(elements)
    # Convert the list to a string
    final_result = ''.join(elements)
    return final_result


if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")

    # Get user input for the number of each type of character
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Generate and print the password. Time complexity for this is O(n)
    password = password_generator(nr_letters, nr_symbols, nr_numbers)
    print(f"Here is your password --> {password}")
