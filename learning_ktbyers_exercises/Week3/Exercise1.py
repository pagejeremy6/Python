"""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""
from pprint import pprint

# read method a file, gives a string
with open("show_vlan.txt") as f:
    show_vlan = f.read()

# construct a new list
list_test = []

# Extract vlan id and vlan name with for loop
# splitlines = split string into a list, each line is a list item
for line in show_vlan.splitlines():
    if "VLAN" in line or "----" in line or line.startswith("  "):
        # continue = continue with next iteration of the loop, skip
        continue
    fields = line.split()
    # Split a string (each item of the list) into a list to break it down further
    vlan_id = fields[0]
    vlan_name = fields[1]
    list_test.append((vlan_id, vlan_name))
    # double paranthese cuz tuple

pprint(list_test)