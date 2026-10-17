
# Parse JSON — JSON to Python

# The json.loads() method converts a JSON string into a Python dictionary.

# Example
import json

# Some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# Parse x:
y = json.loads(x)

# The result is a Python dictionary:
print(y["age"])

# Output:

# 30
# Remember
# import json → imports Python's built-in JSON module.
# json.loads() → converts JSON → Python.
# The result is a Python dictionary.
# y["age"] → gets the value 30.

# Easy way to remember:
# loads() = load JSON string into Python.