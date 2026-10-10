# arr = [10, 20, 30, 40, 50]
# search = 30

# low = 0
# high = len(arr) - 1

# while low <= high:
#     mid = (low + high) // 2

#     if arr[mid] == search:
#         print("Element found at index", mid)
#         break
#     elif arr[mid] < search:
#         low = mid + 1
#     else:
#         high = mid - 1
# else:
#     print("Element not found")

# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

arr.sort()

print("Sorted list:", arr)

search = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == search:
        print("Element found at index", mid)
        break
    elif arr[mid] < search:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")