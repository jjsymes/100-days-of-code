# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names=(name1 + name2).lower()
true_count = 0
love_count = 0

true_count += names.count('t')
true_count += names.count('r')
true_count += names.count('u')
true_count += names.count('e')

love_count += names.count('l')
love_count += names.count('o')
love_count += names.count('v')
love_count += names.count('e')

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
