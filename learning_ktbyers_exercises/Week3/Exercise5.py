"""
[Optional/bonus]
*** Note, to actually test this in your environment, change the test IP addresses to something in
your environment that you can ping successfully. ***
Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or
'10.10.100.'.
You should use the 'range' builtin to accomplish this.
Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.
Use Python's enumerate to print out all of the IP addresses and their corresponding list index.
The output should look similar to the following:
0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...
Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.
Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this
short list. For Windows the command will probably be os.system("ping -n 3 10.10.100.3").
Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be
similar to the following:
WINDOWS = False
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
"""

import os

#string
base_ip = "192.168.23."

my_list = []
base_cmd_windows = "ping -n 2"

# range to build list with for loop
# 192.168.23.1-254
for last_octet in range(1,255):
    new_ip = base_ip + str(last_octet)
    my_list.append(new_ip)

short_list = my_list[2:6]

print("-" * 80)

# ping shorther list of ip
for ip in short_list:
    print("IP is: ", ip)
    return_code = os.system("{} {}".format(base_cmd_windows, ip))
    print("-" * 80)