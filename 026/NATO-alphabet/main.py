student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import os

directory = os.path.realpath(__file__ + f"/{os.pardir}")

csv_file = f"{directory}/nato_phonetic_alphabet.csv"

phonetic_alphabet_df = pandas.read_csv(csv_file)

phonetic_alphabet_dictionary = {row.letter:row.code for (_, row) in phonetic_alphabet_df.iterrows()}

user_input = ""

while user_input != "EXIT":
    user_input = input("Enter a word: ").upper()
    phonetic_list = [phonetic_alphabet_dictionary[letter] for letter in user_input]
    print(phonetic_list)

