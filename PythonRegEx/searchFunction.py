
# The re.search() function searches a string for the first match of a pattern.

# Example
import re

txt = "The rain in Spain"
x = re.search("rain", txt)

print(x)

# Output: Python returns a match object because "rain" is found in the string.

# To print the position where the match starts:

print(x.start())

# Output:

# 4
# Remember

# re.search() → finds the first match.

# x.start() → returns the starting position of the match.

# If no match is found, re.search() returns None.