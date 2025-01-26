from numpy import random
import numpy as np

# generating random numbers
for i in range(0,5):
    print(random.randint(2,20))
    
# generating random numbers with size
arr1 = random.randint(2,20, size=(2,3))
print(arr1)

# generating random float numbers
m = 2
n = 5
arr1 = random.rand(m,n)
print(arr1)

# generating random numbers or strings from given choice
arr1 = random.choice([3,5,7,9], size=(2,3))
print(arr1)

arr2 = random.choice(['arun','kumar','singh'], size=(2,3))
print(arr2)

# generating random permutation of elements
arr1 = np.array([1,2,3,4,5])
print(random.permutation(arr1))
