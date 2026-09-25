
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# Join set1 and set2 into a new set:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set.union(set1, set2)

print(set3)

# ==============================

# You can use the | operator instead of the union() method, and you will get the same result.

# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# ==============================
# Join multiple sets using the union() method:
# All the joining methods and operators can be used to join multiple sets.

# When using a method, just add more sets in the parentheses, separated by commas:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set4 = {"x", "y", "z"}

set5 = set.union(set1, set2, set4)
print(set5)

# ==============================

# The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# ==============================

# Intersection
# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.

# Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


# ==============================

# You can use the & operator instead of the intersection() method, and you will get the same result.

# Example
# Use & to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)



# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.


# ==============================

# The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

# Use the difference_update() method to keep only the items from the first set that are not present in the other set:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)