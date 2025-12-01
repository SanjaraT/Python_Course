list =[1,2,9,16,25,36,49,64,81,100]
x = int(input("Enter the number to be searched: "))
idx = 0
for i in list:
    if (i==x):
        print("X is found at: ", idx)
    idx +=1 