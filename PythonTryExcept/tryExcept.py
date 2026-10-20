
# Python Try Except

# try:
# Test a block of code for errors.

# except:
# Handle the error.

# else:
# Run code when there is no error.

# finally:
# Run code regardless of whether there is an error.


# ==========================
# Basic Try Except

try:
    print(x)
except:
    print("An exception occurred")


# ==========================
# Without Try Except

# print(x)
# This causes a NameError because x is not defined.


# ==========================
# Many Exceptions

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


# ==========================
# Else

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# ==========================
# Finally

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# ==========================
# Finally is useful for cleanup

try:
    f = open("demofile.txt")
    try:
        f.write("Hello")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")