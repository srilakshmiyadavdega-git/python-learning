import keyword
#print all python keywords
print("Python Keywords:")
print(keyword.kwlist)
#print how many keywords are there
print("total number of keywords:",len(keyword.kwlist))

#create variables for age and name
age = 22
name = "srialkshmi"
print("Name:",name)
print("Age:",age)

#create a variables with special symbols
my_name = "srialkshmi"
print(my_name)

#create a variable starting with a number
#1name = "sri"   #error (can not start with a number)
name1 = "sree"
print(name1)

#assign multiple variables to multiple values
name, age, city = "sree", 22, "nellore"
print(name)
print(age)
print(city) 

#assign multiplevariables to one value
a = b = c = 100
print(a)
print(b)
print(c)

#Assign a variable, then re-assign it
age = 22
print("Before:", age)

age = 23
print("After:", age)

#Swap variables in different ways
a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)

#Using Python's tuple unpacking
a = 10
b = 20

a, b = b, a

print(a)
print(b)
#Using addition and subtraction
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a)
print(b)

#Create and delete a variable
name = "Srilakshmi"

print(name)

del name

# print(name)   # Error because the variable is deleted

#Write a single-line comment
# This is a single-line comment

print("Hello Python")

#Write a multi-line comment
"""
This is a multi-line comment.
It can contain multiple lines.
It is used to explain the code.
"""

print("Hello Python")