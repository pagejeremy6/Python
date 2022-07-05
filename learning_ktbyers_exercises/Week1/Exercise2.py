#Exercise2

"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it
up into its octets. Print out the octets in decimal, binary, and hex.
Your program output should look like the following:
$ python exercise2.py
Please enter an IP address: 80.98.150.240
    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             150            240
   0b1515000      0b1150015      0b1150150     0b11115000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------
Four columns, fifteen characters wide, a header column, data centered in the column.
"""

# Prompt a user to enter an ip
my_ipaddr = input("Enter an ip address: ")

# Break into octets
# Split a string into a list, delemeter is the . for each iteam
octets = my_ipaddr.split(".")

# Print out in decimal,binary,hex with formating
# format ^15 = center 15
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-"*55)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print("-"*55)



#bin_0 = bin(int(octets[0]))
#print(bin_0)