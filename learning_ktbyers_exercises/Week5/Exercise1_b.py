"""
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with
a default value of 'cisco_ios'. Print all four of the function variables out as part of the
function's execution.
Call the 'ssh_conn2' function both with and without specifying the device_type
Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
the **kwargs technique.
"""

def ssh_conn_2(ip_addr, username, password, device_type='cisco_ios'):
    print(f"The IP address is: {ip_addr}")
    print(f"The Username is: {username}")
    print(f"The Password is: {password}")
    print(f"The Device Type is: {device_type}")
    return

print()
print("Specify device type:")
ssh_conn_2('192.168.1.1', 'admin', 'password123', 'junos')

print()
print("dont Specify device type:")
ssh_conn_2('192.168.1.1', 'admin', 'password123')

my_dict = {
    'ip_addr': '192.168.1.1',
    'username': 'admin',
    'password': 'pass123',
}

print()
print("with dictionnary")
ssh_conn_2(**my_dict)