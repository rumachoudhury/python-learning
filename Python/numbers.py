
# There are three numeric types in Python:

# int
# float
# complex
# In Python, you must use j (or J) to represent the imaginary part of a complex number.

# =====================================


# Example

x = 10  # int

y = 1.2  #float

z = 1j # complex(no space before j) and must use j no other letter 


# To verify the type of any object in Python, use the type() function:
print(type(x))

print(type(y))

print(type(z))


# ============================================
# Integers:
x = 1
y = 35656222554887711
z = -3255522

print(x, type(x))
print(y, type(y))
print(z, type(z))

# type(x) → tells you what kind of data it is
# x, type(x) → tells you the value + what kind of data it is


# ============================================
# Floats:
x = 1.10
y = 1.0
z = -35.59

print(x, type(x))
print(y, type(y))
print(z, type(z))


# ============================================
# Complex:
x = 3+5j
y = 5j
z = -5j

print(x, type(x))
print(y, type(y))
print(z, type(z))

# ============================================
# Convert from one type to another:

x = 1     #int
y = 2.8   #float
z = 1j    #complex

#convert from 'int' to 'float':
a = float (x)

#convert from 'float' to 'int':
b = int (y)

#convert from 'int' to 'complex':
c = complex (x)


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))