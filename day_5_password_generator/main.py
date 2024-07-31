import string
import random


def password_generator(letters, symbols, numbers):
    elements = []
    elements += [random.choice(string.ascii_letters) for _ in range(letters)]
    elements += [random.choice(string.punctuation) for _ in range(symbols)]
    elements += [str(random.randint(0, 9)) for _ in range(numbers)]

    random.shuffle(elements)
    final_result = ''.join(elements)
    return final_result


if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    letters_amount = int(input("How many letters would you like in your password?\n"))
    symbols_amount = int(input("How many symbols would you like in your password?\n"))
    number_amount = int(input("How many numbers would you like in your password?\n"))

    password = password_generator(letters_amount, symbols_amount, number_amount)

    print(f"Here is your password: {password}")
