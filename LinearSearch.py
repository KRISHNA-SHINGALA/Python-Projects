# arr = [10, 20, 30, 40, 50]
# search = 30

# for i in range(len(arr)):
#     if arr[i] == search:
#         print("Element found at index", i)
#         break
# else:
#     print("Element not found")

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter element to search: "))

for i in range(len(arr)):
    if arr[i] == search:
        print("Element found at index", i)
        break
else:
    print("Element not found")