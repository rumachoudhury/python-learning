
# Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.

my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
print(my_set)

# To add multiple items to a set use the update() method.
my_set.update(["kiwi", "mango"])
print(my_set)

# You can also add items from another set
another_set = {"grape", "pineapple"}
my_set.update(another_set)
print(my_set)