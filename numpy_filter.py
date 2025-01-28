import numpy as np

# np.where()
arr1 = np.array([2,4,1,8])
indices = np.where(arr1 > 3)
print(indices)
# filtering numpy array using indices
print(arr1[indices])
# multiple conditions
arr2 = np.array([1,3,5,7])
indices = np.where((arr2 > 3) & (arr2 < 8))
print(arr2[indices])
# filtering using np.where() and broadcasting
indices = np.where(arr1>arr2)
print(arr1[indices])

# filtering array
arr1 = np.array([1,2,3,4,5,6])
filter_arr = [True,False,True,False,False,True]
print(arr1[filter_arr])
# filtering on one array using another array
ages = np.array([18,24,28,16,13])
names = np.array(['arun','dhruv','sujal','ajay','kk'])
filter = np.where(ages >= 18)
print(names[filter])