#simple logic

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = [
    [0, 0],
    [0, 0]
]

for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j] += A[i][k] * B[k][j]

print(C)

#logic

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

rows_A = len(A)
cols_A = len(A[0])

rows_B = len(B)
cols_B = len(B[0])

# Matrix multiplication is possible only when:
# columns of A == rows of B

if cols_A != rows_B:
    print("Matrix multiplication not possible")

else:

    C = [[0 for j in range(cols_B)] for i in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    print("Result:")

    for row in C:
        print(row)

#user input

# Matrix A size
r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

A = []

print("Enter Matrix A elements:")

for i in range(r1):
    row = []

    for j in range(c1):
        value = int(input())
        row.append(value)

    A.append(row)


# Matrix B size
r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

B = []

print("Enter Matrix B elements:")

for i in range(r2):
    row = []

    for j in range(c2):
        value = int(input())
        row.append(value)

    B.append(row)


# Check multiplication condition
if c1 != r2:
    print("Matrix multiplication is not possible")

else:

    # Create result matrix
    C = [[0 for j in range(c2)] for i in range(r1)]

    # Matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    # Print result
    print("Result Matrix:")

    for i in range(r1):
        for j in range(c2):
            print(C[i][j], end=" ")

        print()

