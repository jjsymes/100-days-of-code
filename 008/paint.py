import math

COVERAGE_PER_CAN = 5

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    number_of_cans = int(math.ceil(number_of_cans))
    print(f"You will need {number_of_cans} cans of paint.")

wall_height = float(input("What is wall height (m)? "))
wall_width = float(input("What is wall width (m)? "))

paint_calc(wall_height, wall_width, COVERAGE_PER_CAN)