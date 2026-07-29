
# Global variables can be used by everyone, both inside of function and outside.

# Creating a variable outside of the function,
# and using it inside the function

x = "awesome" #is a global variable because it is created outside the function.

def myfunc():
    print("Python is " + x)


# now call the function
myfunc() # Output:Python is awesome


# ===================================================
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

# create a variable inside a function, with the same name as global variable but value is different
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is" + x)

# now call the function
myfunc() 