""" with open("pythonf.txt","w") as f:
    f.write("Hi everyone, i am sanjara\nWe are learning file I/O.\nusing java.\nI love programming in java. ") """
""" with open("pythonf.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)

with open("pythonf.txt","w") as f:
    data = f.write(new_data) """
def check_word():
    word = input("Enter the word to be searched: ")
    with open("pythonf.txt","r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")
check_word()
