

# The raise keyword lets you create an exception when a condition occurs.

# Example 1: Raise an Exception
# Raise an error if x is less than 0

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Output:

# Exception: Sorry, no numbers below zero

# Because x is -1, the condition x < 0 is True, so Python raises an exception and stops the program unless the exception is handled.

# Example 2: Raise a TypeError
# Raise a TypeError if x is not an integer

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")

# Output:

# TypeError: Only integers are allowed

# Here, "hello" is a string, not an integer, so Python raises a TypeError.

# Remember

# raise — creates an exception.

# Exception() — raises a general exception.

# TypeError() — raises an error related to an incorrect type.

# Practice: Change x = "hello" to x = 10. What do you think will happen?

