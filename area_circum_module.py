from math import pi

def calc_area(length, width):
    """
    Calculates square footage using area formula of length x width
    """
    area = length*width
    print(f'The square footage is {area}')

# area(7,3)


def circumference(diameter):
    """
    Calculates circumference of a circle using formula of C = pi * diamater  https://www.geeksforgeeks.org/circumference-of-a-circle/
    """
    circum = diameter * pi
    print (f'The circumference is {circum}')

# circumference(2)


# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area
# ------------------------------------------
#2) Has a function to calculate the circumference of a circle

# Program in Jupyter Notebook should take in user input and 
# use imported functions to calculate a circle's circumference or a 
# houses square footage