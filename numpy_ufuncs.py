import numpy as np

# using normal list
list1 = [1,2,3]
list2 = [1,2,3]
result = []
for i in range(0,len(list1)):
    result.append(list1[i]+list2[i])
    
print(result)
# this takes so much time and effort to write the code
# using numpy ufuncs
list1 = np.array([1,2,3])
list2 = np.array([1,2,3])
print(list1 + list2)
print(np.add(list1,list2))

# subtract
print(list1 - list2)
print(np.subtract(list1,list2))

# multiply
print(list1 * list2)
print(np.multiply(list1,list2))

# divide
print(list1 / list2)
print(np.divide(list1,list2))

# power
print(list1 ** list2)
print(np.power(list1,list2))

# modulus
print(list1 % list2)
print(np.mod(list1,list2))

# sum of all values in list1 and list2
print(np.sum([list1,list2]))

# sum of values axis wise
print(np.sum([list1,list2], axis=1))

# product of all values in list1 and list2
print(np.prod([list1,list2]))

# product of values axis wise
print(np.prod([list1,list2], axis=1))

# can be done for single array as well
print(np.prod(list1))
