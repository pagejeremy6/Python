"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the
first and last lines of the output.
From the first line use the string .split() method to obtain the local AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen.
"""

#readlines method a file = gives a list, each line is element of the list
with open("show_ip_bgp_summ.txt") as f:
    output = f.readlines()


# var are element of  a list = string
first_line = output[0]
last_line = output[-1]

# split method method of an index to get required information
# split string = list , each element separated by whitespace
first_line = first_line.split()[-1]
last_line = last_line.split()[0]

print("AS numbers: ", first_line," and IP address: ", last_line)