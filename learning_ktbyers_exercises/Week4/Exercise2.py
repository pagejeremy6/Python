"""
Create three separate lists of IP addresses. The first list should be the IP addresses for the
Houston data center routers and should have over ten IP addresses in it including some duplicate IP
addresses.
The second list should be the Atlanta data center routers and should have at least eight IP
addresses including some that overlap with the Houston data center.
The third list should be the Chicago data center routers and should have at least eight IP
addresses. The Chicago IP addresses have some overlap with the IP addresses in both Houston
and in Atlanta
Convert each of these three lists to a set.
Using set operations, find the IP addresses that are duplicated between Houston and Atlanta.
Using set operations, find the IP addresses that are duplicated in all three sites.
Using set operations, find the IP addresses that are entirely unique in Chicago.
"""

houston_ips = [
    "10.10.1.1",
    "10.10.4.1",
    "10.10.3.1",
    "10.10.4.1",
    "10.10.5.1",
    "10.10.6.1",
    "10.10.7.1",
    "10.10.8.1",
    "10.10.9.1",
    "10.10.10.1",
    "10.10.11.1"
]

atlanta_ips = [
    "10.20.1.1",
    "10.20.2.1",
    "10.20.3.1",
    "10.20.4.1",
    "10.20.5.1",
    "10.20.6.1",
    "10.10.10.1",
    "10.10.11.1"
]

chicago_ips = [
    "10.30.1.1",
    "10.30.2.1",
    "10.30.3.1",
    "10.30.4.1",
    "10.30.4.1",
    "10.10.8.1",
    "10.10.10.1",
    "10.20.5.1",
]

# Convert to sets
set_houston = set(houston_ips)
set_atlanta = set(atlanta_ips)
set_chicago = set(chicago_ips)

# Duplicate Houston-Atlanta
print("Duplicate ip in Houston and Atlanta: ", set_houston & set_atlanta)

# Duplicate Houston-Atlanta-Chicago
print("Duplicate ip 3 sites: ", set_houston & set_atlanta & set_chicago)

# Unique to Chicago
print("Unique to Chicago: ", set_chicago.difference(set_houston.difference(set_atlanta)))