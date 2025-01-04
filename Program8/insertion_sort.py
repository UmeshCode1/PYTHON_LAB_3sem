# Write a python program to perform insertion sort.

#insertion sort = repeatedly taking an element from the unsorted part and inserting it into its correct position in the sorted part.

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr

arr=input("Enter the list of numbers: ").split()
arr = [int(x) for x in arr]

print("Sorted list: ", insertion_sort(arr))
