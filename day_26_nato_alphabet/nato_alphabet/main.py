import pandas

# TODO 1. Create a dictionary in this format: {"A" : "Alpha", ...}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
result = [nato_alphabet[i] for i in user_input]
print(result)
