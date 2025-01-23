# list comprehension
list1 =[i for i in range(1,11)]
print(list1)
# -: using string to create lists
list1 = [i.upper() for i in "Hardik"]
print(list1)
# -: we can do it by using a list too
# -: using nested loops and if statements
list1 = [[1,2,3],[3,4,5],[5,6,7],[7,8,9]]
list2 = [j for i in list1 for j in i if j%2==0]
print(list2)

# set comprehension
s1 = {j for i in list1 for j in i if j%2 == 0}
print(s1)

# dictionary comprehension
dic1 = {i:i**2 for i in range(1,11)}
print(dic1)
# -: reverse key value pair of another dictionary
dic2 = {value:key for key,value in dic1.items()}
print(dic2)
# -: nested dictionary comprehension
dic3 = {i:{j:j**2 for j in range(1,6)} for i in range(1,6)}
print(dic3)
