import numpy as np

# shape of array
# 1D array:
arr = np.array([1,2,3,4])
print(arr.shape)
# 2D array:
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)

# braodcasting(changing the shape of array)
# Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
# Rule 2: If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
# Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

# 1. scalar value can be used to perform arithmetic operations on array
# scalar with 1D array(x,)
scalar = 10
arr = np.array([1,2,3])
print(arr + scalar)
# scalar with 2D array(x,y)
scalar = 10
arr = np.array([[1,2,3],[4,5,6]])
print(arr * scalar)

# 2. arr1(x,y) and arr2(z,) where y=z
arr1 = np.array([[100,200,300,400],[100,200,300,400],[100,200,300,400]])
arr2 = np.array([1,2,3,4])
# arr2(4,) -> arr2(3,4)
print(arr1 + arr2)

# 3. arr1(x,y) and arr2(1,z) where y=z
arr1 = np.array([[100,200,300],[100,200,300],[100,200,300],[100,200,300]])
arr2 = np.array([1,2,3])
# arr2(1,3) -> arr2(4,3)
print(arr1 + arr2)

# 4. arr1(x,) and arr2(y,) where x!=y
# this will produce error
# for example: arr1(4,) and arr2(3,)

# 5. arr1(x,1) and arr2(y,) where x=y
arr1 = np.array([[1],[2],[3]])
arr2 = np.array([100,200,300,400])
# arr2(4,) -> arr2(3,4)
# arr1(3,1) -> arr1(3,4)
print(arr1 + arr2)