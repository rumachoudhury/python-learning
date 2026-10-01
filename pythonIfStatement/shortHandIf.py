
# One-Line if

# If an if statement has only one statement, you can write it on one line.

from doctest import Example


a = 5
b = 2
if a > b: print("a is greater than b")


# ======================================
# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

# Example
# One-line if/else that prints a value:

a = 2
b = 330
print("A") if a > b else print("B") # One-line if/else statement

# ================================
# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:


# Example
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# # ====================================
# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:


# One line, three outcomes:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# =================================
# Python — Setting a Default Value
username = ""

display_name = username if username else "Guest"

print("Welcome,", display_name)
# Output
# Welcome, Guest
# 🧠 Easy meaning
# username if username else "Guest"

# Means:

# If username has a value → use it.
# If it is empty → use "Guest".

# Here username = "" is empty, so Python uses "Guest".