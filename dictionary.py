# creation
# using {} brackets
dic1 = {'Name': "Hardik", "Age": 19}
print(dic1)

# using dict() constructor
list1 = [("Name","Dhruv"),("Age",18)]
dic2 = dict(list1)
print(dic2) # same can be done with tuple

# using variables
dic3 = dict(Name = "Sujal", Age = 20)

# accessing elements
print(dic1["Name"])
print(dic1.get("husn",100))

# updating elements
dic1['Name'] = "Arun"

# adding elements
dic1 ["Salary"] = 10000
print(dic1)

# iteration
for i in dic1.keys():
    print(i)

for i in dic1.values():
    print(i)

for (key,value) in dic1.items():
    print(key,value)

# dictionary operations
dic1.update(dic2)
dic1.pop("Age")
dic1.popitem()
n = len(dic1)
print(dic1)    

# Nested dictionaries
employee_data = {
    'hardik' : {
        'age' : 19
    },
    'ajay' : {
        'age' : 21
    }
}     

# deleting elements
del employee_data['hardik']

for key1,value1 in employee_data.items():
    for key2,value2 in value1.items():
        print(key1,':',key2, ':' ,value2)

           