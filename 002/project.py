print('Welcome to the tip calculator.')
total = float(input('What was the total bill? $'))
number_of_people = int(input('How many people to split the bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
total_each = (total + (total*(tip/100)) )/number_of_people
total_each = "{:.2f}".format(total_each)
print(f"Each person should pay: ${total_each}")
