
# Modify Strings
# Modify Strings = use Python functions to create a new version of a string. ✅
# .upper() → uppercase
# .lower() → lowercase
# .replace() → replace text
# .strip() → remove spaces
# .split() → split into parts

# 1. Change to uppercase
text = "hello"
print(text.upper()) #output will be HELLO

# 2. Change to lowercase
text = "HELLO"
print(text.lower()) #output will be hello

3. Replace part of a string
text = "I like to learn Python"
print(text.replace("Python", "Java")) #output will be I like to learn something new everyday

# 4. Remove extra spaces
text = " Hello "
print(text.strip()) #output will be Hello

# 5. Split a string into parts
text = "I like Python"
print(text.split()) #output will be ['I', 'like', 'Python']

# You can also choose what to split by:
text = "apple,banana,orange"
print(text.split(",")) #output will be ['apple', 'banana', 'orange']

# .split() always returns a list. ✅