# Identity Operators

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


# ===============================
# The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)