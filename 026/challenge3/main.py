import os

directory = os.path.realpath(__file__ + f"/{os.pardir}")

file1 = f"{directory}/file1.txt"
file2 = f"{directory}/file2.txt"

with open(file1, mode="r") as f:
            file_1_numbers = f.read().splitlines()

with open(file2, mode="r") as f:
            file_2_numbers = f.read().splitlines()

result = [int(number) for number in file_1_numbers if number in file_2_numbers]

# Write your code above 👆 LIST OF COMMON NUMBERS IN THE TWO FILES

print(result)


