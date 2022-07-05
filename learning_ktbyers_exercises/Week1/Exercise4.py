"""Create a show_version variable that contains the following
show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "
Remove all leading and trailing whitespace from the string.
Split the string and extract the model and serial_number from it.
Check if 'Cisco' is contained in the model string (ignore capitalization).
Check if '881' is in the model string.
Print out both the serial number and the model.
"""

show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "

# remove trailing/leading whitespace, strip method
show_version = show_version.strip()

# Extract model, sn
# Split a string into a list, use whitespace a delimeter
show_version = show_version.split()
model = show_version[1]
serial_number = show_version[2]

# check if elements are in the variable
vendor_cisco = 'cisco' in model.lower()
model_881 = "881" in model

# print
print("Is Cisco contained in the model {}".format(vendor_cisco))
print("Is 881 contains in the model {}".format(model_881))