#Write a python program to find the square root of a number using Newton's method.

def newton_method(number,number_iters=100):
    a = float(number)
    for i in range(number_iters):
        number = 0.5 * (number + a / number)
    return number
  a=float(input("Enter the first number: "))
  b=float(input("Enter the  second number: "))
  print("The square root of the number is: ",newton_method(a))
  print("The square root of the number is: ",newton_method(b))
  
  
  