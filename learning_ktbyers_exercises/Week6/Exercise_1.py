"""Establish a connection to the network device and print out the device's prompt."""

from netmiko import Netmiko
from getpass import getpass

my_device = {
    "host": "192.168.23.3",
    "username": "admin",
    "password": getpass(),
    "device_type": "aruba_osswitch"
}

net_conn = Netmiko(**my_device)
print(net_conn.find_prompt())

