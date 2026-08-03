
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
# =============================================