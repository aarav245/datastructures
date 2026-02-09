set1 = {12,45,70,72,72,45,12}
print(set1)
#empty set
sete = set()
print(len(set1))
#add
set1.add(76)
print(set1)
#remove
set1.remove(45)
print(set1)
set1.discard(5453)
print(set1)
#member op
print(70 in set1)
#set op 
set2 = {56,904,2232}
set3 = {56,863,2453}
print(set2 | set3) #union
print(set2 & set3) #intersection
print(set2 - set3) #difference
print(set2 ^ set3) #symmetric difference