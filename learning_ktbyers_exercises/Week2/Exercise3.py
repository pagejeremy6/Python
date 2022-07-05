"""Read in the "show_arp.txt" file using the readlines() method. Use a list slice to
remove the header line.
Use pretty print to print out the resulting list to the screen, syntax is:
----
from pprint import pprint
pprint(some_var)
----
Use the list .sort() method to sort the list based on IP addresses.
Create a new list slice that is only the first three ARP entries.
Use the .join() method to join these first three arp entries back together as a single string
using the newline character ('\n') as the separator.
Write this string containing the three ARP entries out to a file named "arp_entries.txt".
"""
from pprint import pprint

# method readlines with a file = return a list, each line is an item of the list
with open("show_arp.txt") as f:
    output = f.readlines()

# slice to remove first element of list
output = output[1:]
pprint(output)

# sort method, sort list alphabetically
print("\n")
output.sort()
pprint(output)

# new list slice only first 3 entries
print("\n")
output = output[0:3]
pprint(output)

# 3 list item are join together into a string, \n is the hash character put between each element
print("\n")
output = "\n".join(output)
print(output)
print(type(output))

# write to a new file
with open("arp_entries.txt", "wt") as f:
    # w=wrinting t=text mode (default)
    f.write(output)
