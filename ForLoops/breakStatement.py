
# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

# Example
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Output:

# apple
# banana
# How it works
# x = "apple" → print apple
# x = "banana" → print banana
# x == "banana" → True
# break → stop the loop
# "cherry" is never printed.