import os
import sys
from art import logo

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

bidders = []

bidding_in_progress = True

while bidding_in_progress == True:
    bidder = {
        "name": "",
        "bid": 0.00
    }
    print("Silent Bidding Application")
    print(logo)
    name = input("What is your name?: ")
    bidder['name'] = name

    input_valid = False
    while input_valid == False:
        try:
            bid = float(input("What is your bid?: $"))
        except ValueError:
            print("Valid number, please")
            continue
        if bid >= 0.00:
            input_valid = True
        else:
            "Bid cannot be a negative number."
    bidder['bid'] = bid

    bidders.append(bidder)

    input_valid = False
    while input_valid == False:
        user_input = input("Are ther any other bidders? [Y/N]: ").lower()
        if user_input == "y" or user_input == 'yes':
            input_valid = True
            bidding_in_progress = True
        elif user_input == "n" or user_input == 'no':
            input_valid = True
            bidding_in_progress = False
        else:
            print("Invalid input")

    clear()



highest_bidder = max(bidders, key=lambda x:x['bid'])

print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}.")
