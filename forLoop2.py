print("PRINT THE MULTIPLICATION TABLE OF A NUMBER")
n = int(input("Enter a number: "))
for i in range(1,11):
    res = n*i
    print(n, "x", i,"=", res)