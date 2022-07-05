"""
Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have
TextFSM automatically convert this show command output to structured data.
"""

from netmiko import Netmiko
from getpass import getpass

my_device = {
    "host": "192.168.23.3",
    "username": "admin",
    "password": getpass(),
    "device_type": 'hp_procurve'
}

net_conn = Netmiko(**my_device)

output = net_conn.send_command("show arp", use_textfsm=True)
print(output)