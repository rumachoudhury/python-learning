

# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# ==============================

# and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.

# ExampleGet your own Python Server
# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")



# ===================================
# or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.

# Example
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")



# ========================================
# The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.

# Test if a is NOT greater than b:

# Python-এ not মানে “না”।

# এটি condition-এর result উল্টে দেয়।

# True → False
# False → True

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")