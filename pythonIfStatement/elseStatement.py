
# The else Keyword

# The else keyword catches anything that was not caught by the previous conditions.

# In simple words:

# If none of the if or elif conditions are True, run the else block.

# Example
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



# ============================
# Checking even or odd numbers:

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")


# ==========================

# Temperature classifier:

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


#   =============================
#   =============================
# Else as Fallback

# else runs when none of the previous conditions are True.

# It is useful for validation, errors, and default actions.

username = "Emil"
if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")


# if → check condition

# else → fallback if condition is False