
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
    print("Python is " + x)

# now call the function

myfunc() 



# ===================================================
# To create a global variable inside a function, you can use the global keyword.
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("python is " + x)


# ===================================================
# Also, use the global keyword if you want to change a global variable inside a function.
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "fantastic"

def myfunc():
    global x
    x = "fun" #The value changes from fantastic to fun

myfunc()

print("Learning python is " + x)  