

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:


x = "John"
# is the same as
x = 'John'


# ===========================================
# Variable names are case-sensitive.


a = 4

A = 4

# A will not overwrite a


# ================================================
# Multi Words Variable Names

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"


# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

# ================================================
# Legal variable names:
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# ================================================
# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# ================================================
# Many Values to Multiple Variables:
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Apple", "Banana"

print(x, y, z)


# ================================================
# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# or
# print(x, y, z)

# or
print("Multiple values:", x, y, z)

# ================================================
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

# ================================================
# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"

print(x, y, z)


# ================================================
# You can also use the + operator to output multiple variables:
# And If you want spaces between words, add spaces inside the strings:
x = "I "
y = "am "
z = "learning Python"

print(x + y + z)



# ================================================
# For numbers, the + character works as a mathematical operator:
x = 5
y = 10

print(x + y) #output will be 15



# When you try to combine a string and a number with +,
# Python will give you a TypeError:

x = 5
y = "John"

print(x + y) #output error



# The best way to output multiple variables is to separate them with commas.
# Commas support different data types:

x = 5
y = "John"

print(x, y) #output will be 5 John

# ================================================