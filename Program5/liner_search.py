# Write a python program to perform linear search.

def linear_search(list, n, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1
  
list = [1,2,Umesh,4, kinshuk ,7,vishal,9,prince]
x=kinsuk
n = len(list)
result = linear_search(list, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index:", result)
    
