#Write a program that takes two float numbers, x and y, and prints x with the sign of y.
# Use the copysign function defined in the math module.

# place `import` statement at top of the program
import math

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
print(math.copysign(x,y))
