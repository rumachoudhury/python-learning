
# Calling a Function
# To call (run) a function, write the function name followed by ().

# Example
def my_function():
  print("Hello from a function")

my_function()



# =============================
# You can call the same function multiple times:

def my_function():
    print("Hello!")

my_function()
my_function()
my_function()

# Output:

# Hello!
# Hello!
# Hello!

# def my_function():  → create the function

# my_function()       → call/run the function

# def = create
# () = call/run


# ================================

# Python — Why Use Functions?

# The main reason to use functions is to avoid repeating the same code.

# Without a Function

# If we need to convert several temperatures, we might repeat the same calculation:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# This works, but the calculation:

# (temp - 32) * 5 / 9

# is repeated again and again.


# =============================

# With a Function

# We can write the calculation once:

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9

# Then use the function whenever we need it:

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Output:

# 25.0
# 35.0
# 10.0

# We can write the code once → use it many times. That's the main benefit of functions.