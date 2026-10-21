
# To check whether a variable contains None, use the identity operators is or is not.

result = None

if result is None:
    print("No result yet")
else:
    print("Result is ready")

# Output:

# No result yet


# Easy way to remember
# is None → checks if the value is None
# is not None → checks if the value is not None

# =============================
# Example:

result = "Success"

if result is not None:
    print("Result is ready")

# Output:

# Result is ready


# ================================
# using is not instead:

result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")

# Output:

# No result yet

# Why? Because result = None, the condition result is not None is False, so Python executes the else block.