weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

def celsius_to_fahrenheit(celsius):
    return 9.0/5.0 * celsius + 32

weather_f = {day:celsius_to_fahrenheit(temp) for (day, temp) in weather_c.items()}

print(weather_f)


