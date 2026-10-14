
# The strftime() method converts a date or time into a readable string using format codes.

# Example: Display the Month Name
# import datetime

import datetime


x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# Output:

# June
# Remember

# strftime() → formats a date or time as text.

# %B → full month name, such as June.

# %b → abbreviated month name, such as Jun.

# %Y → four-digit year, such as 2018.

# %A → full weekday name, such as Friday