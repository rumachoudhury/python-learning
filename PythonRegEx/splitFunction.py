
# Python RegEx — split() Function

# The re.split() function splits a string into a list wherever the pattern matches.

# Example
import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)

print(x)

# Output:

# ['The', 'rain', 'in', 'Spain']
# Remember

# re.split() → splits a string into a list.

# "\s" → matches a whitespace character, such as a space.

# The string is split at each space.

# Easy way to remember: split() breaks one string into multiple pieces.