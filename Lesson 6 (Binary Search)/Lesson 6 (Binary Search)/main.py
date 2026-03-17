list1 = []
user1 = int(input("How many terms would you like to add?"))
for i in range(user1):
    user2 = int(input("What would you like to add? (Use increasing order) "))
    list1.append(user2)
print(list1)
low = 0
high = user1-1
mid = 0
found = False
user3 = int(input("What term would you like to find? "))
while found == False and low <= high:
    mid = low+high//2
    if list1[mid] == user3:
        print("Item was found at",mid+1)
        found = True
    elif list1[mid] < user3:
        low = mid+1
    elif list1[mid] > user3:
        high = mid-1
if found == False:
    print("Item was not found. Please try again.")
