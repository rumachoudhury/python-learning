

# Membership operators are used to test if a sequence is presented in an object:

Description: 
# in--->	Returns True if a sequence with the specified value is present in the object

# not in--->	Returns True if a sequence with the specified value is not present in the object

fruits = ["apple", "banana", "cherry"]
print("orange" not in fruits)

# ========================================

text = "Hello World"

print("H" in text)
print("welcome" not in text)  #---->not in
print("World" in text) #---->in   
print("z" not in text) #---->not in