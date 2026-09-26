# simple logic

arr = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(arr)

print(arr[0][0])
print(arr[1][2])
print(arr[2][1])

# logic

arr = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for i in range(3):
    for j in range(3):
        print(arr[i][j], end=" ")

    print()

# User input

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

arr = []

for i in range(rows):
    row = []

    for j in range(cols):
        value = int(input("Enter element: "))
        row.append(value)

    arr.append(row)

print("2D Array:")

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end=" ")

    print()

