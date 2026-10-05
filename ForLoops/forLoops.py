
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# ExampleGet your own Python Server
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# How it works

# Python takes one item at a time from the list:

# apple   → print
# banana  → print
# cherry  → print

# Here:

# fruits → the list
# for → starts the loop
# x → represents the current item
# in → gets items from fruits
# print(x) → prints each item


# ==============================
# Example with Numbers
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)



# ==============================
# Example with a String

# A string is also iterable:

for letter in "Python":
    print(letter)