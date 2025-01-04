#Write a python program to find exponentation of a number#

# using a math module.

import math

num = int(input("Enter a number: "))
exp = int(input("Enter the exponent: "))
print(f"{num} raised to the power {exp} is {math.pow(num, exp)}")

