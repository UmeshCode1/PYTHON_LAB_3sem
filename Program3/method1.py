# Write a python program to find exponentation of a number 
# using a function.

def exponentation(num, exp):
    return num ** exp
  
num = int(input("Enter a number: "))
exp = int(input("Enter the exponent: "))
print(f"{num} raised to the power {exp} is {exponentation(num, exp)}")

