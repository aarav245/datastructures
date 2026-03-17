list1 = []
size = int(input("What size do you want the list to be? "))
for i in range(size):
    elements = int(input("What would you like to add? "))
    list1.append(elements)
print(list1)
for s in range(size):
    for k in range(0,size-s-1):
        if list1[k] > list1[k+1]:
            temp = list1[k]
            list1[k] = list1[k+1]
            list1[k+1] = temp
print(list1)
