def show_element(list,idx):
    if (idx == len(list)):
        return
    print (list[idx])
    return show_element(list,idx+1)
fruits = ["Apple", "Bannana","Mango","Jackfruit","Papaya"]
print(show_element(fruits,0))