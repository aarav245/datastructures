list1 = []
number = int(input("How many things would you like to add? "))
for i in range(number):
    values = int(input("What number would you like to add? "))
    list1.append(values)
print(list1)
#insertion sort
for k in range(1,number):
    keyelement = list1[k]
    j = k-1
    while j >= 0 and list1[j] > keyelement:
        list1[j+1] = list1[j]
        j-=1
    list1[j+1] = keyelement
print(list1)