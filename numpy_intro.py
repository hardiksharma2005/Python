import numpy as nplol

# creating using list
list1 = [1,2,3]
arr1 = nplol.array(list1)
print(arr1)
print(arr1.shape)

# creating using multidimensional list
list2 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = nplol.array(list2)
print(arr2)
print(arr2.shape)

# creating using tuple
tuple1 = (1,2,3)
arr1 = nplol.array(tuple1)
print(arr1)
print(arr1.shape)

# creating a numpy array with zeroes
arr1 = nplol.zeros((2))
print(arr1)
arr2 = nplol.zeros((2,3))
print(arr2)

# creating a numpy array with ones
arr1 = nplol.ones((2))
print(arr1)
arr2 = nplol.ones((2,3))
print(arr2)

# creating an array with diagonal elements set to 1 rest 0
arr1 = nplol.eye(3)
print(arr1)
arr2 = nplol.eye(3,4)
print(arr2)

# creating an array with n elements which are equally differentiated
arr1 = nplol.linspace(1,10,6) # start,end,size
print(arr1)

# creating an array with n elements with specified step size
arr1 = nplol.arange(1,10,2) #start,end,step
print(arr1)