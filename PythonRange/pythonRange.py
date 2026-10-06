

# Creating Ranges

# The range() function can take 1, 2, or 3 arguments:

# range(start, stop, step)

# One Argument
for x in range(5):
    print(x)


# Output:

# 0
# 1
# 2
# 3
# 4

# With one argument:

# range(5)

# means start at 0, stop before 5.

# =================================
# 2. Two Arguments
for x in range(2, 6):
    print(x)

# Output:

# 2
# 3
# 4
# 5
# range(2, 6)
# 2 → start
# 6 → stop (not included)

# ===================================
# 3. Three Arguments
for x in range(2, 10, 2):
    print(x)

# Output:

# 2
# 4
# 6
# 8
# range(2, 10, 2)
# 2 → start
# 10 → stop (not included)
# 2 → step (increase by 2)
# Easy Rule
# range(stop)
# range(start, stop)
# range(start, stop, step)

# Remember: the stop number is never included.

# =======================================
# Using ranges
# Ranges are often used in for loops to iterate over a sequence of numbers.

# Example
# Iterate over each value in a range:

for i in range(10):
  print(i)