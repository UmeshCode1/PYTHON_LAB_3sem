#Write a python program to perform selection sort.

#selection sort = repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning.

def selection_sort(arr):
  
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr

arr=input("Enter the list of numbers: ").split()
arr = [int(x) for x in arr]

print("Sorted list: ", selection_sort(arr))


