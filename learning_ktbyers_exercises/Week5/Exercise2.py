"""
Create a function that randomly generates an IP address for a network. The default base network
should be '10.10.10.'. For simplicity the network will always be a /24.
You should be able to pass a different base network into your function as an argument.
Randomly pick a number between 1 and 254 for the last octet and return the full IP address.
You can use:
import random
random.randint(1, 254)
to randomly generate the last octet.
Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.
For each function call print the returned IP address to the screen.
"""

import random

def gen_ip(base_net, random_ip):
    print(f"the IP generated is :{base_net}{random_ip}")

ran_ip = random.randint(1, 254)

gen_ip("10.10.10.", ran_ip)

# Other way to do it

def gen_ip_2(network="10.10.10."):
    last_octet = str(random.randint(1, 254))
    return network + last_octet

print(gen_ip_2())
print(gen_ip_2("192.168.1."))
print(gen_ip_2(network='172.16.33.'))