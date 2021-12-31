# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
valid_word = False
while valid_word == False:
    try:
        word = input("Enter a word: ").upper()
        for letter in word:
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                raise ValueError("Input should only contain alphabetical characters.")
    except ValueError as e:
        print(e)
    else:
        valid_word = True
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)


# Alternative
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Input should only contain alphabetical characters.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()