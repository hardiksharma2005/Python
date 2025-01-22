tuple1 = tuple([1,2,3])
tuple2 = (4,5,6)
tuple3 = ([1,2,3], True,1,1.9,{1,2,3})

# tuple operations
a,b,c = tuple2
print(a,b,c)
print(tuple1[0])
print(tuple1+tuple2)
print(sum(tuple1))
print(tuple1*3)
print(max(tuple1))
del tuple1