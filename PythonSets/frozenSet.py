
# A frozenset is an immutable version of a set.
# It contains unique, unordered elements.
# Unlike a normal set, you cannot add or remove items.

my_frozenset = frozenset({"apple", "banana", "cherry"})

print(my_frozenset)

# You can check if an item exists
print("apple" in my_frozenset)
print("orange" in my_frozenset)

# Output will look something like:

# {'apple', 'banana', 'cherry'}
# True
# False