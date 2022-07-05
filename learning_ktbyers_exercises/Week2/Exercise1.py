#!/usr/bin/env python
"""Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file
contents to a variable. Print out the file contents to the screen. Also print out the type of the
variable (you should have a string at this point).
Close the file.
Open the file a second time using a Python context manager (with statement). Read in the file
contents using the .readlines() method. Print out the file contents to the screen. Also print out
the type of the variable (you should have a list at this point).
"""

# Open file and use read method, give back a string
f = open("show_version.txt")
output = f.read()
print(output)
print(type(output))
f.close()

# open a file and read it as with statement
# method readlines = return a list, each line is an item of the list
with open("show_version.txt") as g:
    output2 = g.readlines()
print(output2)
print(type(output2))