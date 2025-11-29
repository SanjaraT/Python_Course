nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number to be matched: "))
idx = 0
while idx < len(nums):
    if (nums[idx]==x):
        print("Found at index: ", idx)
    idx += 1  