
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.
# For example:

a = 33
b = 200
if b > a:
  print("b is greater than a")



#   ======================
# Checking if a number is positive:

number = 15
if number > 0:
  print("The number is positive")



#   ========================
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# ❌ If statement, without indentation 
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error


# ✅ If statement, with proper indentation

a = 33
b = 200
if b > a:
  print("b is greater than a") # this will work correctly



# =================================
# Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")