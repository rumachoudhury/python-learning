# Using a Package
# Once the package is installed, it is ready to use.

# Import the "camelcase" package into your project.

# Example
# Import and use "camelcase":

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
# Find Packages
# Find more packages at https://pypi.org/.

# Remove a Package
# Use the uninstall command to remove a package:

# Example
# Uninstall the package named "camelcase":

# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase
# The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:

# Uninstalling camelcase-02.1:
#   Would remove:
#     c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase-0.2-py3.6.egg-info
#     c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase\*
# Proceed (y/n)?
# Press y and the package will be removed.