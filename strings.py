
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# You can display a string literal with the print() function:

print("Hello")
print('Hello')

# ================================================

# Quotes Inside Quotes
# You can use quotes inside a string

print("He is called 'Johnny'")
print('He is called "Johnny"')
print("My name is 'Ruma'")


# ================================================
# Assign String to a Variable

a = "Hello"
print(a)


# ================================================

# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

# -------------------------------------------------

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

# ================================================

# Strings are Arrays
a = "Hello, World!"
print(a[1])

b = "Welcome to python"
print(b[6])


# ================================================
# Looping Through a String

for x in "banana" :

    print(x)


for x in "Learning python is fun" :

    print(x)