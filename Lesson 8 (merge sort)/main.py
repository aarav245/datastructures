list1 = []
size = int(input("How big would you like the list to be? "))
for i in range(size):
    values = int(input("What would you like to add? "))
    list1.append(values)
print(list1)
if len(list1) > 1:
    mid = len(list1)//2
    left = list1[:mid]
    right = list1[mid:]
    left.sort()
    right.sort()
print(left)
print(right)