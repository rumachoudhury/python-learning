
# Slicing Strings
# Slicing means getting part of a string.


# =============================================

# String:  H  e  l  l  o  ,     W  o  r  l  d  !
# Index :  0  1  2  3  4  5  6  7  8  9 10 11 12
# The slice:   b[2:5]
# means:
# Start at index 2 ✅ (l)
# Stop before index 5 ❌ (, is not included)
# Output:  llo


# For example:
b= "Hello, world!"
print(b[0:5]) # Output: Hello
print(b[7:12]) # Output: world
print(b[2:5]) # Output: llo

# Get the characters from the start to position 5 (not included):
print(b[:5]) # Output: Hello

# Get the characters from position 2, and all the way to the end:
print(b[2:]) # Output: llo, world!

# =============================================

# Negative Indexing
# Negative indexes count from the end of the string instead of the beginning.

# Positive indexes:
# H  e  l  l  o  ,     W  o  r  l  d  !
#  0  1  2  3  4  5  6  7  8  9 10 11 12

# Negative indexes:
# H  e  l  l  o  ,     W  o  r  l  d  !
# -13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# -5 → o ✅ (start here)
# -2 → d ❌ (stop before this)

b = "Hello, World!"
print(b[-5:-2]) # Output: orl

# =============================================
