

# Python allows for user input.

# That means we are able to ask the user for input.

# The following example asks for your name, and when you enter a name, it gets printed on the screen:

# ExampleGet your own Python Server
# Ask for user input:

print("Enter your name:")
name = input()
print(f"Hello {name}")

# ===================================
# Using prompt
# In the example above, the user had to input their name on a new line. The Python input() function has a prompt parameter, which acts as a message you can put in front of the user input, on the same line:

# Example
# Add a message in front of the user input:

name = input("Enter your name:")
print(f"Hello {name}")

# =======================================

# Multiple Inputs
# You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:

# Example
# Multiple inputs:

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")