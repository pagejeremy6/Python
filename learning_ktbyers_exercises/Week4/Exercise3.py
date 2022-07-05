"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.
Your output should look as follows:
          OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
     Config Register: 0x2102
"""

import re

# Read file as a string
with open("show_version.txt") as f:
    output = f.read()

show_version = output.splitlines()

conf_register = (re.search(r"^Configuration register is (.*)$", output, flags=re.M).group(1))
serial_number = (re.search(r"^Processor board ID (.*)$", output, flags=re.M).group(1))
os_version = (re.search(r"^ROM.*Version (\S+),.*$", output, flags=re.M).group(1))


print("{:>20}: {:15}".format("OS Version: ", os_version))
print("{:>20}: {:15}".format("Serial Number: ", serial_number))
print("{:>20}: {:15}".format("Config Register: ", conf_register))