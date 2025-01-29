import pandas as pd

# create a series in pandas
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

# indexing in pandas series
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s2)

#create a series from a dictionary
data = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40, 'e' : 50}
s3 = pd.Series(data)
print(s3)