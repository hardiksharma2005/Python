def function_name():
    print("hello")
    
function_name()

# function with arguments    
def function_name(x):
    return x + 1
    
print(function_name(5))

# function with arbitrary arguments
# *args is used to pass a variable number of arguments to a function
def function_name(*ar):
    for i in ar:
        print(i)

function_name(1,2,3)  

# **kwargs is used to pass a variable number of keyword arguments to a function
def function_name(**kwarg):
    for key,value in kwarg.items():
        print(key,"-",value)
        
function_name(Name = "Hardik", Age = 19)    

# nested functions
def function_name(x):
    def function_name1():
        return x + 1
    return function_name1()

print(function_name(5))

# dictionary as arguments
def function_name(dic):
    dic[1] = "hello"

dic = {}
function_name(dic)
print(dic)

# same thing can be done with list and set, but not with tuple 