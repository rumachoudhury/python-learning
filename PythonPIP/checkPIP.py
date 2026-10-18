# Python PIP

# PIP is a package manager for Python.
# It is used to install and manage Python packages.

# Check PIP version:
# pip3 --version

# Install a package:
# pip3 install camelcase

# Use the package:
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# Find Python packages:
# https://pypi.org/

# Remove a package:
# pip3 uninstall camelcase



# ======================
# Important

# The W3Schools example uses Windows:

# C:\Users\Your Name\...

# Since you're using a Mac, you normally don't need to navigate to the Python Scripts folder. You can run:

# pip3 --version

# and:

# pip3 install camelcase

# If you want to actually practice this lesson, run:

# pip3 install camelcase