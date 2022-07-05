"""
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement
outside of your function (i.e. where you have your function calls).
Inside of pdb, experiment with:
1. Listing your code.
2. Using 'next' and 'step' to walk through your code. Make sure you understand the difference
   between the two.
3. Experiment with 'up' and 'down' to move up and down the code stack.
4. Use p <variable> to look at a variable.
5. Set a breakpoint and run your code to the breakpoint.
6. Use '!command' to change a variable (for example !new_mac = [])
"""


import re
import pdb

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

pdb.set_trace()
normalize_mac(mac_address)
