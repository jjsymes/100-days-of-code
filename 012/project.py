from art import logo
from random import randint

HARD_MODE_GUESS_NUMBER = 5
EASY_MODE_GUESS_NUMBER = 10

def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = randint(1, 100)
    guess = None

    valid_input = False
    while not valid_input:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty in ["easy", "e", "hard", "h"]:
            valid_input = True
        else:
            pass

    if difficulty[0] == "e":
        number_of_attempts = EASY_MODE_GUESS_NUMBER
    else:
        number_of_attempts = HARD_MODE_GUESS_NUMBER

    attempts_remaining = number_of_attempts

    while attempts_remaining > 0 and guess != number:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        valid_input = False
        while not valid_input:
            try:
                guess = int(input("Make a guess: "))
                valid_input = True
            except ValueError:
                print("Not a valid number!")
                pass

        if guess == number:
            print(f"You got it. The number was {number}.")
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")

        attempts_remaining -= 1
        if attempts_remaining > 0 and guess != number:
            print("Guess again.")
        elif attempts_remaining == 0 and guess != number:
            print("You have run out of guesses. You lose.")
    return

game()