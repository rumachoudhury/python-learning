
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

my_set = {"apple", "banana", "cherry"}

# Loop through the set items
for item in my_set:
    print(item)

# Check if a specified value is present in the set
print("apple" in my_set)
print("orange" in my_set)

# Check if a specified value is NOT present
print("apple" not in my_set)
print("orange" not in my_set)