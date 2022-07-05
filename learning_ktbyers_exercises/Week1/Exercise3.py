"""Create three different variables: the first variable should use all lower case characters with
underscore ( _ ) as the word separator. The second variable should use all upper case characters
with underscore as the word separator. The third variable should use numbers, letters, and
underscores, but still be a valid variable Python variable name.
Make all three variables be strings that refer to IPv6 addresses.
Use the from future technique so that any string literals in Python2 are unicode.
compare if variable1 equals variable2
compare if variable1 is not equal to variable3
"""

# from future string literal in python2 are unicode instead of ascii
from __future__ import unicode_literals

# Create 3 ipv6 variable
var_ipv6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
VAR2_IPV6 = "8a93:d9ad:0ad1:ad21:9212:3212:1231:1234"
var3_ipv6 = "2001::1023"

# compare them
print("Is var1 equal var2: {}".format(var_ipv6 == VAR2_IPV6))
print("Is var1 not equal to var2: {}".format(var_ipv6 != var3_ipv6))
