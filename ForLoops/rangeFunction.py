
# Python — range() Function

# The range() function is commonly used with a for loop to repeat code a specific number of times.


### Basic Example

# Basic Example
for x in range(6):
    print(x)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5

# Why does it stop at 5?

# range(6) starts at 0 and stops before 6.

# 0 → 1 → 2 → 3 → 4 → 5

# So:

# range(6)

# means:

# Start at 0 and go up to, but not including, 6.

# ==========================
# Start and End

# You can give range() two numbers:

for x in range(2, 6):
    print(x)

# Output:

# 2
# 3
# 4
# 5

# range(2, 6) means:

# Start at 2, stop before 6.