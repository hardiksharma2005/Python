# basic modifying function
def modify(x):
    return x**2

list1 = [1,2,3,4,5]
modified_list = list(map(modify,list1))
print(modified_list)

# using lambda function
lambda_modify = lambda x: x**2

modified_list = list(map(lambda_modify,list1))
print(modified_list)

# using multiple arguments
lambda_modify2 = lambda x,y: x + y

list_added = list(map(lambda_modify2,list1,list1))
print(list_added)

print(list1+list1)