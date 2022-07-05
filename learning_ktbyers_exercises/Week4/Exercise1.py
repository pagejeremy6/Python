"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""
# create dictionnary for a network device 3 key-value pairs
dic1 = {'ip_addr':'192.168.1.1', 'vendor':'cisco', 'username':'jeremy'}

#Print ip_addr key from dictionnary
print("The IP is: ", dic1['ip_addr'])

# if vendor=cisco -> platform=ios, if vendor=juniper -> platform=junos
if dic1['vendor'] == 'cisco':
    dic1['platform'] = 'ios'
elif dic1['vendor'] == 'juniper':
    dic1['platform'] = 'junos'
else:
    dic1['platform'] = 'something else'

# create dictionnary for a bgp, 3 key-value pairs
dic2 = {'bgp_as':'65005', 'peer_as':'65000', 'peer_ip':'10.0.0.1'}

# update method add dic bgp to network device dic
dic1.update(dic2)

# for loop, print dic keys
for key in dic1:
    print(key)

# single for loop, print all keys and values
for key, value in dic1.items():
    print("the key is: ", key, " | the value is: ", value)
