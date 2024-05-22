# First step is to import the math module. The math module contains all mathematical functionalities.
import math

radius = float(input())

area = (radius**2) * math.pi

rounded_area = round(area, 2)

print(rounded_area)