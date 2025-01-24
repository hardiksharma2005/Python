# basic lambda function
# basic function
def cube(y):
    return y*y*y

print(cube(5))
# using lambda function
lambda_cube = lambda y: y*y*y
print(lambda_cube(5))

# lambda function using if and else
lambda_if_else = lambda a,b: a if a > b else b

print(lambda_if_else(5,6))

# lambda function using for loop
lambda_for = lambda lis: any(num < 0 for num in lis)

print(lambda_for([1,2,3,-4,5]))
   