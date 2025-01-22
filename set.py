set1={1,2,3}
set2=set([1,2,3,4,5])

for i in set1:
    print(i)
    
# set operations
set_union = set1.union(set2)
print(set_union)

set_intersection = set1.intersection(set2)
print(set_intersection)

set_difference = set1.difference(set2)
print(set_difference)

set_symmetric_diff = set1.symmetric_difference(set2)
print(set_symmetric_diff)

# set inbuilt functions
set1.add(4)
set1.remove(4)
element_removed = set1.pop()
print(element_removed)
print(set1)

print(set1.isdisjoint(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))

# set conversion
list1 = list(set1)
print(list1) 

