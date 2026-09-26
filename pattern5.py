a = int(input("Enter the number of rows: "))

print ("")

for i in range(1, a+1):
    x = i*(i+1)//2
    for j in range(1, i+1):
        print(x, end = " ")
        x -= 1
    print() 

# output:
# 1
# 3 2
# 6 5 4
