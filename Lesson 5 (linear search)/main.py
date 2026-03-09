list1 = []
nfound = False
count = 0
userinput = int(input("How many items would you like to add? "))
for i in range(userinput):
    user2 = int(input("What items would you like to add? "))
    list1.append(user2)
print(list1)
user3 = int(input("What term would you like to find? "))
for u in range(len(list1)):
    if list1[u] == user3:
        print("Found at",u+1)
        count = count+1
        nfound = True
if nfound == False:
    print("Item was not found! Please try again!")
print("The item was found ",count," times." )


