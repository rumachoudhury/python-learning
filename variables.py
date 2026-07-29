

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