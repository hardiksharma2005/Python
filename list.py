# list formation
list1=[1,2,3,4]
print(list1)
list2 = list([1,2,3,4])
print(list2)
print(list1[0:3])

# multidimensional list
list3 = [[1,2,3],[4,5,6]]
print(list3[0][0])

# list operations
list1.append(5)
print(list1)
last_element =list1.pop()
print(last_element)
list1.insert(2,10)
print(list1)
list1.pop(2)
print(sum(list1))
print(max(list1))
print(min(list1))
print(sorted(list1))
list1.extend(list2)
print(list1)

#string to list and vice versa
string1 = "hello"
list1 = string1.split('l')
print(list1)
string2 = "l".join(list1)
print(string2)

for i in range(0,len(list1)):
    print(list1[i],end = " ")
    
print()

for i in range(0,len(list3)):
    for j in range(0,len(list3[i])):
        print(list3[i][j],end = "")