"""Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list.
"""
# list 5 ip
ip_list = ['192.168.1.1', '10.1.1.1', '172.16.1.1', '205.0.1.2', '130.120.12.4']

# list methods
print("\n" + "Append method")
ip_list.append('1.1.1.1')
print(ip_list)

print("\n" + "Extend method")
ip_list.extend(['8.8.8.8', '9.9.9.9'])
print(ip_list)

print("\n" + "Concatenation method")
ip_list = ip_list + ['2.2.2.2', '3.3.3.3']
print(ip_list)

print("\n" + "First element")
print(ip_list[0])

print("\n" + "Last element")
print(ip_list[-1])

print("\n" + "pop first")
ip_list.pop(0)
print(ip_list)

print("\n" + "pop last")
ip_list.pop(-1)
print(ip_list)

print("\n" + "insert begining")
ip_list.insert(0, "2.2.2.2")
print(ip_list)