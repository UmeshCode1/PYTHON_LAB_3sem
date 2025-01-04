# WAP to find GCD of two numbers.

# # Method 3
#using ecluid's algorithm

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a =int(input("Enter the first number: "))
b =int(input("Enter the second number: "))

print("The GCD of two numbers is: ",gcd(a,b))
