print("--PROGRAM TO CHECK PALINDROME OR NOT--")
sen = input("Enter a sentence separated by spaces: ")
sen_list = sen.split()
sen_list2 = sen_list.copy()
sen_list2.reverse()
if (sen_list2 == sen_list):
    print("Palindrome")
else:
    print("Not Palindrome")