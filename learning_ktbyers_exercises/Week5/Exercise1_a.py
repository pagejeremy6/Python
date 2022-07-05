"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.
Call this ssh_conn function using entirely positional arguments.
Call this ssh_conn function using entirely named arguments.
Call this ssh_conn function using a mix of positional and named arguments.
"""

def ssh_conn(ip_addr, username, password):
    print(f"The IP address is: {ip_addr}")
    print(f"The Username is: {username}")
    print(f"The Password is: {password}")
    return

print()
print("Positional argument")
ssh_conn('192.168.1.1', 'admin', 'pass123')
print()

print()
print("named argument")
ssh_conn(ip_addr='192.168.1.1', password='pass123', username='admin')
print()

print()
print("Mix of postional and named arguments")
ssh_conn('192.168.1.1', password='pass123', username='admin')
print()

