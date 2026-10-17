
# The json.dumps() method converts a Python object into a JSON string.

# Example
import json

# A Python object (dictionary):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert into JSON:
y = json.dumps(x)

# The result is a JSON string:
print(y)

# Output:

# {"name": "John", "age": 30, "city": "New York"}
# Remember
# json.dumps() → Python → JSON
# json.loads() → JSON → Python
# dumps = convert to a JSON string