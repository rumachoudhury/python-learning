
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