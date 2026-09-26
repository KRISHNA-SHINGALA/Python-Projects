# Take number of rows from user
n = int(input("Enter number of rows: "))

# Pattern
for i in range(1, n + 1):

    # First row
    if i == 1:
        print("1 1")
        continue

    # Print numbers from 1 to i-1
    for j in range(1, i):
        print(j, end=" ")

    # Print odd number at the end
    print(2 * i - 1)

# OUTPUT
# 1 1
# 1 2 3
# 1 2 3 5
# 1 2 3 4 7
# 1 2 3 4 5 9
# 1 2 3 4 5 6 11