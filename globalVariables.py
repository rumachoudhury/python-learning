
# Global variables can be used by everyone, both inside of function and outside.

# Creating a variable outside of the function,
# and using it inside the function

x = "awesome" #is a global variable because it is created outside the function.

def myfunc():
    print("Python is " + x)


# now call the function
myfunc()