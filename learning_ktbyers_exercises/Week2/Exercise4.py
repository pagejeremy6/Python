"""Read in the "show_ip_int_brief.txt" file into your program using the
.readlines() method.
Obtain the list entry associated with the FastEthernet4 interface. You can
just hard-code the index at this point since we haven't covered for-loops
or regular expressions:
Use the string .split() method to obtain both the IP address and the
corresponding interface associated with the IP.
Create a two element tuple from the result (intf_name, ip_address).
Print that tuple to the screen.
Use pycodestyle on this script. Get the warnings/errors to zero. You might need
to 'pip install pycodestyle' on your computer (should be able to type this from
the shell prompt). Alternatively, you can type:
  'python -m pip install pycodestyle'.
"""
from pprint import pprint

# readlines method a file = as a list, each line is an element of the list
with open("show_ip_int_brief.txt") as f:
    output = f.readlines()

# list index put as string into a variable
int_4 = output[5]
print(int_4)

# string split by whitespace, gives strings
int_4 = int_4.split()

# Create 2 element tuple and print
int_4 = int_4[0:2]
my_tuple = tuple(int_4)
print(my_tuple)
