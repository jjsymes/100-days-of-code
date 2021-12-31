import random
import string

desired_letter_count = int(input("How many letters would you like in your password?\n"))
desired_symbol_count = int(input("How many symbols would you like in your password?\n"))
desired_number_count = int(input("How many numbers would you like in your password?\n"))

total_length = desired_letter_count + desired_symbol_count + desired_number_count

password_characters = []

for i in range(desired_letter_count):
    password_characters.append(random.choice(string.ascii_letters))

for i in range(desired_symbol_count):
    password_characters.append(random.choice(string.punctuation))

for i in range(desired_number_count):
    password_characters.append(random.choice(string.digits))

random.shuffle(password_characters)

password = ""

for char in password_characters:
    password += char

print(f"Here is your password: {password}")

password = ""

while len(password_characters) != 0:
    random_index = random.randint(0, len(password_characters) - 1)
    password += password_characters.pop(random_index)


print(f"Here is your password: {password}")
