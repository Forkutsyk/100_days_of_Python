import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    user_input = input("Enter a word: ").upper()
    try:
        result = [nato_alphabet[i] for i in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(result)
        break
