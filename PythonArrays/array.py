# An array is a special variable, which can hold more than one value at a time.

# An array is used to store multiple values in a single variable.

# In Python, lists are commonly used to store collections of items. For arrays with specific data types, Python also has the array module.

# Example 1 — Store Car Names in a List
cars = ["Ford", "Volvo", "BMW"]

print(cars)


# ====================
# Python — Access Array Elements

# You can access an array or list element by using its index number.




# Example 1 — Get the First Item
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)

# Output:

# Ford

# cars[0] gets the first item because Python indexing starts at 0.

# ==============================
# Python — Length of an Array (len())

# The len() function returns the number of elements in an array or list.

# Example 1 — Count Car Names
cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)

# Output:

# 3

# ==================
# Example 2 — Print the Length Directly
cars = ["Toyota", "Honda", "BMW", "Tesla"]

print(len(cars))

# Output:

# 4