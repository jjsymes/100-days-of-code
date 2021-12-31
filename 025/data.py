with open("weather_data.csv") as f:
    data = f.read().splitlines()

print(data)

import csv

temperatures = []

with open("weather_data.csv") as f:
    data = csv.reader(f)
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])
print(type(data["temp"]))
print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday_temp = data[data.day == "Monday"].temp

def celsius_to_fahrenheit(celsius):
    return 9.0/5.0 * celsius + 32

print(celsius_to_fahrenheit(int(monday_temp)))