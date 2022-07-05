"""
Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following
format:
01:23:45:67:89:AB
This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
The function should have one parameter, the mac_address. It should return the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:
a:b:c:d:e:f
should be converted to:
0A:0B:0C:0D:0E:0F
Write several test cases for your function and verify it is working properly.
"""

import re

# MAC Format : 01:23:45:67:89. Function 1 parameter
# Handle lower/uper case conversion
# convert 0000.aaaa.bbbb
# convert 00-00-aa-aa-bb-bb
# Single digits , zero-padded to 2 digts.

print()
print("MAC Converter")
print('''
accepted format:
- 0000.aaaa.bbbb
- aa:bb:cc:ee:ff:gg
- aa-bb-cc-dd-ee-ff
'''
)


mac_address = input("Enter your MAC: ")

def normalize_mac(mac_address):
    # will put letter upercase
    mac_address = mac_address.upper()
   # if mac contains character : or - 
    if "-" in mac_address or ":" in mac_address:
        new_mac = []
        # Create a list, delemeter is either : or -
        octets = re.split(r"[-|:]", mac_address)

        # Iterate over element of list (octet)
        for octet in octets:
            # if lenght is lower than 2 add 0 at beginning
            # zfill add zero to the left. len of char - zfill = zero added
            # if len = 1 , 2-1 = 1 , one zero added
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    elif "." in mac_address:
        mac_address = mac_address.upper()
        mac_address = mac_address.split(".")
        mac_address = "".join(mac_address)

        new_mac = []

        while len(mac_address) > 0:
            entry = mac_address[:2]
            mac_address = mac_address[2:]
            new_mac.append(entry)
     
    final_mac = (":".join(new_mac))
    print(final_mac)
    return


normalize_mac(mac_address)
