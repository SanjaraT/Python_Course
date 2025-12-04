""" with open("pythonf.txt","w") as f:
    f.write("Hi everyone, i am sanjara\nWe are learning file I/O.\nusing java.\nI love programming in java. ") """
with open("pythonf.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)

with open("pythonf.txt","w") as f:
    data = f.write(new_data)
