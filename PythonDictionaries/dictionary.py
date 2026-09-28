

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