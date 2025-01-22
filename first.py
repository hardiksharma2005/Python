print("hello")
print(1+2)

# use of '\n'
print("hello\nworld")

# use of '\t'
print("hello\tworld")

# declaration of variables and use
name = "hardik"
what = "awaits"
print("hello {} world {}".format(name,what))

# data type
x = 3 + 2j
print(x)
print(complex(1,2))

# type casting
x = 1
a = float(x)

# arithmetic operations
print(3+2)
print(complex(1,2) + complex(3,4))

# complex number operations
z = 3 + 4j
y = 1 - 2j
# conjugate of z
conj_z = z.conjugate()
print(conj_z)
# real and imaginary part of y
real_y = y.real
imag_y = y.imag
print(real_y, imag_y)
# magnitude of z
mag_z = abs(z)
print(mag_z)

# string operations
string1 = "hello"
string2 = "world"
print(string1 + string2)
replicated_string = string1*3
print(replicated_string)
print(string1[-1])
# slicing
print(string1[1:3])
print(string1[::-1])
# length of sting
print(len(string1))
# split
print(string1.split('l'))

# bool operations
a = True
b = False
print(a and b)
a = 1
b = 1
print ("is a equal to b: ", a == b)
print(a==b and y==z)

# if elif else
if 10 > 20:
    print("10 is greater than 20")
elif 10 < 20:
    print("10 is less than 20")
else:
    print("10 is equal to 20")
    
# for loop
string = "data#avengers#"
for i in string:
    print(i,end = " ")
print()
# indexing
for i in range(0,len(string)):
    if string[i] == "#":
        print(i)

print()
# while loop
c = 0
while c != len(string):
    if string[c] == "#":
        print(c)
    c+=1

print()

# None
a = None
print(a) 
if a:
    print("a is true")
elif a is False:
    print("a is false")
else:
    print("a is None")