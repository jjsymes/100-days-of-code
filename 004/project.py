from hashlib import scrypt
import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = input("What do you choose? rock paper or scissors?\n")

if user_input == "rock" or user_input == "r" or user_input == "0":
    choice = "rock"
    print(ROCK)
elif user_input == "paper" or user_input == "p" or user_input == "1":
    choice = "paper"
    print(PAPER)
elif user_input == "scissors" or user_input == "s" or user_input == "2":
    choice = "scissors"
    print(SCISSORS)
else:
    print(f"{user_input} not an option. Please play again!")
    exit()

computer_choice=random.randint(0,2)

print("\nComputer chose:\n")

if computer_choice == 0:
    computer_choice = "rock"
    print(ROCK)
elif computer_choice == 1:
    computer_choice = "paper"
    print(PAPER)
else:
    computer_choice = "scissors"
    print(SCISSORS)

if choice == computer_choice:
    print("Draw")
elif (choice == "rock" and computer_choice == "scissors") or (choice == "paper" and computer_choice == "rock") or (choice == "scissors" and computer_choice == "paper"):
    print("You win")
else:
    print("You lose")
