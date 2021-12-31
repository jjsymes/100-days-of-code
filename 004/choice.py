# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

number_of_people = len(names)
choice_index = random.randint(0, number_of_people - 1)
choice = names[choice_index]

print(f"{choice} is going to buy the meal today...")

print(f"No, actually {random.choice(names)} will buy the meal today!")
