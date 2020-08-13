"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
args = sys.argv
print("args another way:", args)
sys.argv[0] = 'arg1, ar2, arg3'
for x in sys.argv[0].split():
    print("Arg item:", x)
print("Number of arguments: ", len(sys.argv[0]))

# Print out the OS platform you're using:
# YOUR CODE HERE
import platform

print("Platform name:", platform.system())
# Print out the version of Python you're using:
# YOUR CODE HERE


import os

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Current process ID:", os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current working directory:", os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print("Machine login name:", os.getlogin())
# OR use getpass
import getpass

print("User login name:", getpass.getuser())
