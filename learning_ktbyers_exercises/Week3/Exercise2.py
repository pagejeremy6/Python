"""
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this
file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a
separate variable.
Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the
string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.
Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then
print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.
Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have
found both of these devices, 'break' out of the for loop.
"""

from pprint import pprint

# read method of a file gives a string
with open("show_arp.txt") as f:
    show_arp = f.read()

arp_list = []
found1, found2 = (False, False)

# splitlines = split string into a list, each line is a list item
for line in show_arp.splitlines():
    if "Protocol" in line:
        continue
    # line is a string
    fields = line.split()
    # split a string (each item of the list) into a list to break it down by word
    ip_addr = fields[1]
    mac_addr = fields[3]
    #print("not found")
    
    # if element are found print stuff
    if "10.220.88.1" in ip_addr:
        print("Default gateway IP/Mac: ", ip_addr, "|", mac_addr)
        found1 = True
    
    elif "10.220.88.30" in ip_addr:
        print("Arista3 IP/MAC is: ", ip_addr, "|", mac_addr)
        found2 = True
    # if both element found, break of loop
    if found1 and found2:
        print("Exiting..")
        break

