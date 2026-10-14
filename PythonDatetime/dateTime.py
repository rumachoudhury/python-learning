

# Python's datetime module helps you work with dates and times. You can use it to get the current date and time.

# Example
import datetime

x = datetime.datetime.now()
print(x)



# import datetime — imports Python's built-in datetime module.

# datetime.datetime.now() — gets the current local date and time.

# print(x) — displays the result.

# ==============================
# Python Datetime — Year and Weekday

# This code prints the current year and the name of the current weekday.

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))