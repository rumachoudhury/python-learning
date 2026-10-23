

# What is a Virtual Environment?
# A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

# It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

# Think of a virtual environment as a separate container for each Python project. Each container:

# Has its own Python interpreter
# Has its own set of installed packages
# Is isolated from other virtual environments
# Can have different versions of the same package
# Using virtual environments is important because:

# It prevents package version conflicts between projects
# Makes projects more portable and reproducible
# Keeps your system Python installation clean
# Allows testing with different Python versions

# =====================================
# Creating a Virtual Environment
# Python has the built-in venv module for creating virtual environments.

# To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:

# ExampleGet your own Python Server
# Run this command to create a virtual environment named myfirstproject:

# macOS
# $ python -m venv myfirstproject

# ========================================
# This will set up a virtual environment, and create a folder named "myfirstproject" with subfolders and files, like this:

# Result
# The file/folder structure will look like this:

# myfirstproject
#   Include
#   Lib
#   Scripts
#   .gitignore
#   pyvenv.cfg

# ===========================================
# Activate Virtual Environment
# To use the virtual environment, you have to activate it with this command:

# Example
# Activate the virtual environment:

# macOS
# $ source myfirstproject/bin/activate
# After activation, your prompt will change to show that you are now working in the active environment:

# ==============================================
# Result
# The command line will look like this when the virtual environment is active:

# macOS
# (myfirstproject) ... $


# ================================================
# Install Packages
# Once your virtual environment is activated, you can install packages in it, using pip.

# We will install a package called 'cowsay':

# Example
# Install 'cowsay' in the virtual environment:

# macOS
# (myfirstproject) ... $ pip install cowsay

# ==================================================
# Result
# 'cowsay' is installed only in the virtual environment:

# Collecting cowsay
#   Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
# Downloading cowsay-6.1-py3-none-any.whl (25 kB)
# Installing collected packages: cowsay
# Successfully installed cowsay-6.1

# [notice] A new release of pip is available: 25.0.1 -> 25.1.1
# [notice] To update, run: python.exe -m pip install --upgrade pip

# =============================================



# Using Package
# Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.

# Create a file called test.py on your computer. You can place it wherever you want, but I will place it in the same location as the myfirstproject folder -not in the folder, but in the same location.

# Open the file and insert these three lines in it:

# Example
# Insert two lines in test.py:

# from PythonVirtualEnvironment import cowsay_example


# Try it in your Python file

# Create a file named cowsay_example.py and add:

# import cowsay

# cowsay.cow("Hello Ruma!")
# cowsay.trex("I am learning Python!")
# Then, try to execute the file while you are in the virtual environment:

# Example
# Execute test.py in the virtual environment:

# macOS
# (myfirstproject) ... $ python test.py


# ============================================
# rumachoudhury@MacBookAir python-learning % python3 -m venv .venv
# print(f"Hello {name}")
# rumachoudhury@MacBookAir python-learning % print(f"Hello {name}")
# zsh: invalid mode specification
# rumachoudhury@MacBookAir python-learning % source .venv/bin/activate
# (.venv) rumachoudhury@MacBookAir python-learning % python -m pip install cowsay
# Collecting cowsay
#   Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
# Downloading cowsay-6.1-py3-none-any.whl (25 kB)
# Installing collected packages: cowsay
# Successfully installed cowsay-6.1

# [notice] A new release of pip is available: 26.2.1 -> 26.2.2
# [notice] To update, run: pip install --upgrade pip
# (.venv) rumachoudhury@MacBookAir python-learning % python -c "import cowsay; cowsay.cow('Hello Ruma!')"
#   ___________
# | Hello Ruma! |
#   ===========
#            \
#             \
#               ^__^
#               (oo)\_______
#               (__)\       )\/\
#                   ||----w |
#                   ||     ||
# (.venv) rumachoudhury@MacBookAir python-learning % 



# =====================================================

# Deactivate Virtual Environment
# To deactivate the virtual environment use this command:

# Example
# Deactivate the virtual environment:

# macOS
# (myfirstproject) C:\Users\Your Name> deactivate


# As a result, you are now back in the normal command line interface:

# Result
# Normal command line interface:

# WindowsmacOS/Linux
# C:\Users\Your Name>
# If you try to execute the test.py file outside of the virtual environment, you will get an error because 'cowsay' is missing. It was only installed in the virtual environment:



