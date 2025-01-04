# Write a python program to perform merge sort.

# Merge sort = repeatedly dividing the array into two halves and then merging them in a sorted manner.

def merge_sort(arr):
  print("Splitting ", arr)
  if len(arr) > 1:
    mid = len(arr)//2
    lefthand = arr[:mid]
    righthand = arr[mid:]
    merge_sort(lefthand)
    merge_sort(righthand)
    
    i = j = k = 0
    
    while i < len(lefthand) and j < len(righthand):
      if lefthand[i] < righthand[j]:
        arr[k] = lefthand[i]
        i += 1
      else:
        arr[k] = righthand[j]
        j += 1
      k += 1
      
    while i < len(lefthand):
      arr[k] = lefthand[i]
      i += 1
      k += 1
      
    while j < len(righthand):
      arr[k] = righthand[j]
      j += 1
      k += 1
      
  print("Merging ", arr)
  return arr

arr=input("Enter the list of numbers: ").split()
arr = [int(x) for x in arr]

print("Sorted list: ", merge_sort(arr))
    