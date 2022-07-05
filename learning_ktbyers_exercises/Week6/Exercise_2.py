"""
Use send_command() to send a show command down the SSH channel. Retrieve the results and print the
results to the screen.
"""

from netmiko import Netmiko
from getpass import getpass

my_device = {
    "host": "192.168.23.3",
    "username": "admin",
    "password": getpass(),
    "device_type": "aruba_osswitch"
}

net_conn = Netmiko(**my_device)
command = "show interfaces brief"

output = net_conn.send_command(command)
print(output)