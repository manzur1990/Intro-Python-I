"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
# IMPORTS:
import getpass
import os
import sys
import platform

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for arg in sys.argv:
    print(arg)

print("this is the name of the program", sys.argv[0])
print("Argument List:", str(sys.argv))

print("Number of element exluding the name of the program:", (len(sys.argv)-1))

# Print out the OS platform you're using:
# YOUR CODE HERE


# print(os.name)
print(platform.system())


# Print out the version of Python you're using:
# YOUR CODE HERE

print(platform.release())

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

# print("[Process ID]:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE

# print("[current working directory]:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE


# print("Local Machine's Username:", getpass.getuser())
