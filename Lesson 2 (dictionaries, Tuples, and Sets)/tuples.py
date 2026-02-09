tuple1 = (15,32,68,79)
print(tuple1)
#tuple length
print(len(tuple1))
tuple2 = (10,)
print(type(tuple2),type(tuple1))
#indexing
print(tuple1[2])
print(tuple1[-3])
#looping through a tuple
for i in tuple1:
    print(i)
#tuple unpacking
var1,var2,var3,var4 = tuple1
print(var1)
print(var2)
print(var3)
print(var4)
