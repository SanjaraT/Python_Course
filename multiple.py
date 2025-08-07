print("--PROGRAM TO FIND X IS MULTIPLE OF N OR NOT--")
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

if (x % n == 0):
    print(x, "is a multiple of ",n)
else:
    print(x, "is not a multiple of ",n)