# write a program to which will read a int and perform the sum of digits of that int

a = int(input("Enter an integer: "))

sum = 0
while a > 0:
    d = a % 10
    sum += d
    a //= 10

print("The sum of the digits is:", sum)