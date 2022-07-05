"""
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
"""



#read method of a file, gives a string
with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()

found1, found2 = (False, False)

# loop until you encountered elements, save into variable
#splitlines split a string into a list, each line is a list item
for line in show_lldp.splitlines():
    if "System Name" in line:
        line = line.split()
        #split each string(list item), is split on whitespace, by word
        sys_name = line[2]
        found1 = True

    elif "Port id" in line:
        line = line.split()
        #split each string(list item), is split on whitespace, by word
        port_id = line[2]
        found2 = True
    #break if both found
    if found1 and found2:
        print(sys_name)
        print(port_id)
        break
