

mylist = ["apple", "banana", "cherry"]
print(mylist)

# ============================================

# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# ============================================

# List Length
# To determine how many items a list has, use the len() function:


# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# ================================================

# List Items - Data Types

list1 = ["apple", "banana", "cherry"]   # Strings
list2 = [1, 5, 7, 9, 3]                 # Integers
list3 = [True, False, False]            # Booleans

print(list1)
print(list2)
print(list3)

# Output
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]

# ===================================================

# Python list can contain multiple data types at the same time.

list4 = ["abc", 34, True, 40, "male"]

print(list4)

# Data types in this list:
# "abc" → String (str)
# 34 → Integer (int)
# True → Boolean (bool)
# 40 → Integer (int)
# "male" → String (str)

# Output:
# ['abc', 34, True, 40, 'male']