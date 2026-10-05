
# Python — continue in a for Loop

# The continue statement skips the current item and moves to the next item in the loop.


# Example
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue

    print(x)

# Output:

# apple
# cherry
# How it works
# x = "apple" → print apple
# x = "banana" → condition is True
# continue → skip banana
# x = "cherry" → print cherry

# So "banana" is not printed.