a = int(input("Enter the number of rows: "))

print("")

# for i in range(1, a+1):
#     for j in range(1, i+1):
#         print(j%2 , end = "")
#     print()

for i in range(1, a+1):
    for j in range(1, i+1):
        if j%2 == 0:
            print(0, end = "")
        else:
            print(1, end = "")
    print()

# output:
# 1
# 10
# 101
# 1010
# 10101