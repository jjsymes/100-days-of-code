# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == 'S':
    price = 15
elif size == 'M':
    price = 20
elif size == 'L':
    price = 25
else:
    print("Invalid size selected!")
    exit()

if add_pepperoni == 'Y':
    if size == 'S':
        price += 2
    else:
        price +=3
elif add_pepperoni != 'N':
    print("Invalid option for pepperoni selected!")
    exit()

if extra_cheese == 'Y':
    price += 1
elif extra_cheese != 'N':
    print("Invalid option for extra cheese selected!")
    exit()

print(f"Your pizza costs ${price}")
