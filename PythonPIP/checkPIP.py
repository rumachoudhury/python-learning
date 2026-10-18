
# PIP stands for Pip Installs Packages. It is Python’s package manager, used to install and manage additional Python packages (libraries).

# 1. Check if PIP is installed
# pip --version

# On your Mac, you can also use:

# pip3 --version
# 2. Install a package

# For example, install requests:

# pip install requests

# or:

# pip3 install requests
# 3. Upgrade a package
# pip install --upgrade requests
# 4. List installed packages
# pip list

# Simple example
import requests

response = requests.get("https://www.google.com")
print(response.status_code)


# Here, requests is not built into Python, so we install it using PIP.

# If you're following the W3Schools Python PIP lesson, send me your next example and I'll explain it in the same simple style.