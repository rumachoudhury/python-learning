
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36

# This will be error

txt = "My name is Ruma, I am " + age

print(txt)

# =============================================

# F-Strings
# But we can combine strings and numbers by using f-strings or the format() method!
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 36

txt = f"My name is Ruma, I am {age} years old"

print(txt)

# =============================================