"""
Read the 'show_ipv6_intf.txt' file.
From this file use Python regular expressions to extract the two IPv6 addresses.
The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of
the literal characters in the IPv6 address.
From this, create a list of IPv6 addresses that includes only the above two addresses.
Print this list to the screen.
"""
import re

with open ("show_ipv6_intf.txt") as f:
    output = f.read()

# without DOTALL
match = (re.search(r"^\s+IPv6 .*$\n\s+(?P<ipv6_1>\S+) \[VALID\]$\n\s+(?P<ipv6_2>\S+).*$", output, flags=re.M))
var_ipv6_1 = match.groupdict()['ipv6_1']
var_ipv6_2 = match.groupdict()['ipv6_2']

print(type(var_ipv6_1), var_ipv6_1)
print(type(var_ipv6_2), var_ipv6_2)


list_ipv6 = []
list_ipv6 = list_ipv6 + [var_ipv6_1, var_ipv6_2]
print("Without DOTALL method: ", list_ipv6)


# with DOTALL .* DOES match new line
# no need to specificy ^. paranthesis are matching whitespace+ ipv61 + ipv62 + whitespace
#print(re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet:", output, flags=re.DOTALL).group(1))
match_2 = (re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet:", output, flags=re.DOTALL))

# Extract content between paranthesis and remove whitespace
ipv6_addresses = match_2.group(1).strip()
#print(ipv6_addresses)

# make it a list
list_ipv6_2 = ipv6_addresses.splitlines()
#print(list_ipv6_2)

# remove VALID
# re.sub = regex to substitute VALID by nothing
for i, address in enumerate(list_ipv6_2):
    #print(i, address)
    address = re.sub(r"\[VALID\]", "", address)
    #print(address)
    list_ipv6_2[i] = address.strip()

print("With DOTALL method: ", list_ipv6_2)