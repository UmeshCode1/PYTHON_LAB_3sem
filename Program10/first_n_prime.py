# Wirte a python program to print first n prime numbers

num = int(input("Enter the range: "))
print("prime Numbers are: ", end = " ")
for n in range(1, num + 1):
  for i in range(2,n):
    if n % i == 0:
      break
  else: 
    print(n, end = " ")
    