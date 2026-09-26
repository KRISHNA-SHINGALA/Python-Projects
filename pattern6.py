a = int(input("Enter the number of rows: "))

#    *
#   * *
#  * * *
# * * * *
#* * * * *

for i in range(1, a+1):
    for j in range(a-i):
        print(" ", end = "")
    for k in range(1, i+1):
        print("*", end = " ")
    print()