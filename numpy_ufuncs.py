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
arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])
print(arr1 + arr2)
print(np.add(arr1,arr2))

# subtract
print(arr1 - arr2)
print(np.subtract(arr1,arr2))

# multiply
print(arr1 * arr2)
print(np.multiply(arr1,arr2))

# divide
print(arr1 / arr2)
print(np.divide(arr1,arr2))

# power
print(arr1 ** arr2)
print(np.power(arr1,arr2))

# modulus
print(arr1 % arr2)
print(np.mod(arr1,arr2))

# sum of all values in arr1 and arr2
print(np.sum([arr1,arr2]))

# sum of values axis wise
print(np.sum([arr1,arr2], axis=1))

# product of all values in arr1 and arr2
print(np.prod([arr1,arr2]))

# product of values axis wise
print(np.prod([arr1,arr2], axis=1))

# can be done for single array as well
print(np.prod(arr1))
