# # empty array
# int = []
# print ("Empty array - int = []")

# # same value
# arr = [0] * 5
# print (arr)

# # create and print array
# arr = [10, 20, 30, 40, 50]
# print (arr)

# # fetch value using index
# print(arr[0])
# print(arr[-1])

# # fetch length or value using length 
# print(len(arr))
# print(len(arr) - 1)
# print(arr[len(arr) - 1])

# arr[2] = 100
# print(arr)

# # print array in different type
# arr = [10, 20, 30, 40, 50]

# for i in range(len(arr)):
#     print(arr[i])

# for value in arr:
#     print(value)

# for i in range(len(arr)):
#     print(arr[i])

# # user input array
# n = int(input("Enter size: "))

# arr = []

# for i in range(n):
#     value = int(input("Enter element: "))
#     arr.append(value)

# print(arr)

# # append

# arr = []

# arr.append(10)
# arr.append(20)
# arr.append(30)

# print (arr)

# # reverse array

# arr = [1, 2, 3, 4, 5]
# arr.reverse()
# print(arr)

# # replacement array

# arr = [10, 20, 30, 40, 50]

# left = 0
# right = len(arr) - 1

# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]

#     left += 1
#     right -= 1

# print(arr)

# # LINEAR SEARCH

# arr = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]

# n = int(input("Enter no. :"))

# found = False

# for i in range(len(arr)):
#     if arr[i] == n:
#         print("Found at index:", i)
#         found = True
#         break

# if not found:
#     print("Not Found")

# # BINARY SEARCH
# arr = [10, 20, 30, 40, 50, 60, 70, 1, 2, 3, 4, 5]

# target = int(input("Enter element to search: "))

# left = 0
# right = len(arr) - 1

# while left <= right:

#     mid = (left + right) // 2

#     if arr[mid] == target:
#         print("Element found at index:", mid)
#         break

#     elif arr[mid] < target:
#         left = mid + 1

#     else:
#         right = mid - 1

# else:
#     print("Element not found")

# # BUBBLE SORT

# arr = [5, 3, 8, 1, 2]

# n = len(arr)

# for i in range(n):
#     for j in range(0, n - i - 1):

#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print("Sorted array:", arr)

# Take size from user

n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

for i in range(n):
    for j in range(0, n - i - 1):

        if arr[j] > arr[j + 1]:
            # Swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)