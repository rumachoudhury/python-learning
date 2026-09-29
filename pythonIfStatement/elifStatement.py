
# The elif Keyword

# The elif keyword means:

# "If the previous condition was not True, try this condition."

# It allows you to check another condition after an if statement.

# Example
a = 33
b = 33

if b > a:
    print("b is greater than a")

elif a == b:
    print("a and b are equal")



# What happens?

# First, Python checks:

# b > a

# 33 > 33 is False.

# So Python moves to the elif condition:

# a == b

# 33 == 33 is True.

# Therefore, Python prints:

# a and b are equal

# 🧠 Easy Way to Remember
# if condition1:
#     # Do this

# elif condition2:
#     # Otherwise, try this

# if → elif → elif → else



# ============================
# Testing multiple conditions:

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")