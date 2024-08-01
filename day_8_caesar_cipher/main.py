import art


def caesar(plain_text, shift_amount, cipher_direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            new_char = alphabet[new_position]

            if is_upper:
                new_char = new_char.upper()
            end_text += new_char
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


if __name__ == "__main__":

    end_of_game = False
    print(art.logo)

    while not end_of_game:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ['encode', 'decode']:
            print("Invalid direction.")
            continue
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
        user_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if user_choice == 'no':
            end_of_game = True
            print("Goodbye")
