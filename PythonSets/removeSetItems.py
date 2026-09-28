

# To remove an item in a set, use the remove(), or the discard() method.

my_set = {"apple", "banana", "cherry"}

# Remove an item using remove()
my_set.remove("banana")
print(my_set)

# Remove an item using discard()
my_set.discard("cherry")
print(my_set)

# Remove an item using pop()
my_set.pop()
print(my_set)

# Clear all items from the set
my_set.clear()
print(my_set)