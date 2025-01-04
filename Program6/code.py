#Write a python program to perform binary serach.

#Binary search is a fast search algorithm with run-time complexity of Ο(log n). This search algorithm works on the principle of divide and conquer. For this algorithm to work properly, the data collection should be in the sorted form.

def binary_search(arr, iteam):
    beg, end = 0, len(arr) - 1
    while beg <= end:
        mid = beg + (end - beg) // 2
        if arr[mid] == iteam:
            return mid
        elif arr[mid] > iteam:
            end = mid - 1
        else:
            beg = mid + 1
    return -1
    a = int(input("Enter the number of elements in the list: "))
    b = input("Enter the elements separated by space: ").split()
    arr = []
    for i in b:
        arr.append(int(i))
    arr.sort()
    print("Sorted list is: ", arr)
    iteam = int(input("Enter the number to search: "))
    location = -1
    location = binary_search(arr, iteam)
    if location != -1:
        print(f"Element found at location: {location}")
    else:
        print("Element not found")

  