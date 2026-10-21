

# Functions that do not explicitly return a value return None by default.

# Example
# A function without a return statement returns None:

def myfunc():
  x = 5

x = myfunc()
print(x)



# Output:

# None
# Why does it print None?

# myfunc() runs and assigns 5 to the local variable x.

# The function does not have a return statement.

# Python automatically returns None.

# The returned value is stored in the outside variable x.

# print(x) displays None.