
# With the while loop we can execute a set of statements as long as a condition is true.

# ExampleGet your own Python Server
# Print i as long as i is less than 6:

from doctest import Example


i = 1
while i < 6:
  print(i)
  i += 1


# ==============================

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# ==============================

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# ==============================

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# ==============================
# while + else examples.

# Countdown
count = 3

while count > 0:
    print(count)
    count -= 1
else:
    print("Done!")

# =================================
# Find a number
i = 1

while i <= 5:
    print(i)

    if i == 5:
        print("Found 5!")

    i += 1
else:
    print("Loop finished")