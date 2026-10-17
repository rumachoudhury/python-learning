

# RegEx means Regular Expression. It is used to search, match, and work with patterns in text.

# Python has a built-in module called re.

# Import the re Module
# import re
# Example
import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)

print(x)
# What does ^The.*Spain$ mean?
# ^ → starts with
# The → must start with "The"
# .* → any characters in between
# Spain → must contain/end with "Spain"
# $ → ends with

# So this searches for a string that starts with "The" and ends with "Spain".

# Because "The rain in Spain" matches, re.search() returns a match object.

# Remember
# re.search() → searches for a pattern in a string

# re is built into Python, so you don't need to install anything.