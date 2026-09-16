
# Set items can be of any data type:

set1 = {"apple", "banana", "cherry"}

set2 = {1, 5, 7, 9, 3}

set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

# set3 will only contain True and False because duplicate False is automatically removed.

# ================================

# A set can contain different data types:


# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# =================================
# The set() Constructor
# It is also possible to use the set() constructor to make a set.


# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)