a = int(input("Enter the number of rows: "))

print ("")

k = 1
for i in range(1, a+1):
    for j in range(1, i+1):
        print(k, end = " ")
        k += 1
    print() 

# output:
# 1
# 2 3   
# 4 5 6
