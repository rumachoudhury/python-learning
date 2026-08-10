
print(10 > 9)

print(10 == 9)

print(10 < 9)



# ========================================
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
    print("b is greater then a")
else:
    print("b is not greater then a")


# ============================================
# Evaluate Values and Variables

# Evaluate a string and a number:
print(bool("hello"))
print(bool(15))

# ============================================
# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# ============================================
# lists, tuples, sets, and dictionaries are generally True when they contain something, and False when they are empty.

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# ============================================
# You can create functions that return a Boolean value:

def myFunction(): #Create the function
    return True #Return True

print(myFunction()) #Call the function

# ============================================
# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction()
   return True

if myFunction():
   print("YES")
else:
    print("No")


# ============================================
# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))