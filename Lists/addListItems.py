

# Python - Add List Items
# Append Items
# Using the append() method to append an item:

addlist = ["apple", "banana", "cherry"]

addlist.append("orange")

print(addlist)

# Output:

# ['apple', 'banana', 'cherry', 'orange']


# ====================================

# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# ===========================================

# Extend List
# To append elements from another list to the current list, use the extend() method.

# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)