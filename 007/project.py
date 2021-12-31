import random

WORD_LIST=["HANGMAN", "ELEPHANT", "TURBINE"]
word = random.choice(WORD_LIST)

guessed_letters = []
fail_count=0

while True:
    print(f"Guessed letters: {guessed_letters}")
    print(f"Number of fails: {fail_count}/7")
    guessed_word = ""
    for char in word:
        if char in guessed_letters:
            guessed_word += char
        else:
            guessed_word += "_"
    if word in guessed_letters:
        guessed_word = word
    print(guessed_word)
    if guessed_word == word:
        print("YOU WIN!")
        exit()
    if fail_count == 7:
        print("You LOSE!")
        exit()
    
    guess = input("Guess a letter: ").upper()
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    if (guess not in word) and (guess != word):
        fail_count += 1
