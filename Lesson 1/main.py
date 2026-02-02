#creating a list
list1 = [1,"name",5,6,9,2]
print(list1)
#indexing
print(list1[1])
print(list1[4])
print(list1[-2])
#modifying an existing item
#list1[5] = 8
#print(list1)
#input1 = int(input("Which index number would you like to modify?"))
#input2 = int(input("What new message would you like to add?"))
#list1[input1] = input2
print(list1)
#how to add a new item
list1.append(5)
print(list1)
#adding items at a certain pos
list1.insert(2,"age")
print(list1)
#adding multiple items
list1.extend([2,30,156,78])
print(list1)
#deleting items
#removing through an index
list1.pop(6)
print(list1)
#removing through value
list1.remove(5)
print(list1)
#seeing how many items are in a list
items = len(list1)
print(items)
#iterating the list
for i in list1:
    print(i)
for l in range(10):
    print(list1[l])