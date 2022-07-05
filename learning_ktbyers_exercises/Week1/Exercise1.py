#Exercise 1

"""Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing
three corresponding IP addresses). Print these three variables to standard output using a single
print statement.
Make your print statement compatible with both Python2 and Python3.
If you are using either Linux or MacOS make your program executable by adding a shebang line and
by changing the files permissions (i.e. chmod 755 exercise1.py).
"""
# make print statement compatible python2-3
from __future__ import print_function

# Declare 3 string variable
ip_addr1 = '192.168.1.1'
ip_addr2 = '172.16.1.1'
ip_addr3 = '10.0.0.1'

# print all in one statement
print(ip_addr1, ip_addr2, ip_addr3)