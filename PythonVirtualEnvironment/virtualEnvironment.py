

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

# smacOS
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
