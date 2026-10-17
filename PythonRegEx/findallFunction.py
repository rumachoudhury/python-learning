
# The re.findall() function returns a list of all matches found in a string.

# Example
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)

print(x)

# Output:

# ['ai', 'ai']
# Remember

# re.findall("ai", txt) searches for every occurrence of "ai".

# "ai" appears twice: in "rain" and "Spain".

# findall() returns all matches in a list.

# If no matches are found, it returns an empty list: [].