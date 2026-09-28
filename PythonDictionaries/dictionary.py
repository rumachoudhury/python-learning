

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)


# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(thisdict["brand"])  # Accessing the value associated with the key "brand"
print(thisdict["model"])  # Accessing the value associated with the key "model"
print(thisdict["year"])   # Accessing the value associated with the key "year"


# ======================================

# Dictionaries cannot have two items with the same key:

# Example
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# ==========================================

# Dictionary Length
# To determine how many items a dictionary has, use the len() function:

# Example
# Print the number of items in the dictionary:

print(len(thisdict))


# ==========================================
# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# Example
# String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)  # Accessing the entire dictionary to see all data types

# 4 different value types:
# "brand" → string
# "electric" → boolean
# "year" → integer
# "colors" → list

# ==========================================


# The dict() constructor is another way to create a dictionary.

# The dict() Constructor
# You can use dict() to create a dictionary.

thisdict = dict(name="John", age=36, country="Norway")

print(thisdict)

# Output:

# {'name': 'John', 'age': 36, 'country': 'Norway'}
# One thing to remember

# These two approaches create dictionaries:

# Using {}
thisdict = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# and:

# Using dict()
thisdict = dict(name="John", age=36, country="Norway")