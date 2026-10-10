
# An iterator lets you go through items one at a time.

# Two important functions are:

# iter() → creates an iterator
# next() → gets the next item

mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Output:

# apple
# banana
# cherry


# How It Works

# First, we have an iterable:

# mytuple = ("apple", "banana", "cherry")

# Then we create an iterator:

# myit = iter(mytuple)

# Now myit remembers where it is.

# Each time we use:

# next(myit)

# Python gives us the next item.

# next() → apple
# next() → banana
# next() → cherry

# Iterator vs Iterable

# Iterable = something you can loop through.

# Examples:

# list
# tuple
# set
# dictionary
# string


# =========================
# Iterator = the object that gives you the items one at a time.

# Think of it like:

# Iterable
#    ↓
# iter()
#    ↓
# Iterator
#    ↓
# next() → item
# next() → item
# next() → item