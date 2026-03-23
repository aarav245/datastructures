list1 = []
size = int(input("How big would you like the list to be? "))
for i in range(size):
    values = int(input("What would you like to add? "))
    list1.append(values)
print(list1)
def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left = list1[:mid]
        right = list1[mid:]
        left.sort()
        right.sort()
        i = 0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i+=1
            else:
                list1[k] = right[j]
                j+=1
            k+=1
        #remaining elements
        while i < len(left):
            list1[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            list1[k] = right[j]
            j+=1
            k+=1
mergesort(list1)
print(list1)

#print(left)
#print(right)