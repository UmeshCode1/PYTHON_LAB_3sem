# WAP to find GCD of two numbers.

# # Method 2
# #without using recursion

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a =int(input("Enter the first number: "))
b =int(input("Enter the second number: "))
print("The GCD of two numbers is: ",gcd(a,b))

