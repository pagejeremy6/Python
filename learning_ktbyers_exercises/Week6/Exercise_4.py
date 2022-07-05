"""
Use send_config_set() and send_config_from_file() to make configuration changes.
The configuration changes should be benign. For example, on Cisco IOS I typically change the
logging buffer size.
As part of your program verify that the configuration change occurred properly. For example, use
send_command() to execute 'show run' and verify the new configuration.
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

cfg_commands = [ 'vlan 200', 'vlan 300']
output = net_conn.send_config_set(cfg_commands)
print(output)

output_2 = net_conn.send_command("show vlan | inc [2-3]00")
if '200' in output_2 and '300' in output_2:
    print("Success!")
print(output_2)

output_3 = net_conn.send_config_from_file("config.txt")
print(output_3)