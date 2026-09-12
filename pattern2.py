a = int(input("Enter the number of rows: "))

print("")

# for i in range(1, a+1):
#     for j in range(1, i+1):
#         print(i-j+1 , end = "")
#     print()

for i in range(1, a+1):
    for j in range(i, 0, -1):
        print(j, end = "")
    print()

# output:
# 1
# 21
# 321
# 4321