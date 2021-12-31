# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
LIFE_EXPECTANCY_WEEKS = 4680

age_in_weeks = int(age)*52

weeks_left = LIFE_EXPECTANCY_WEEKS - age_in_weeks
days_left = weeks_left * 7
months_left = weeks_left // 4

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")