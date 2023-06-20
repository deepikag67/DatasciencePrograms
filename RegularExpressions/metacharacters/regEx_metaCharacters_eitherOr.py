# It acts as an operator.
# It checks the pattern before or after the "or" symbol present in the string
# a|b matches any string containing a or b such as axb, adb

import re
s = "axb"
f = re.findall(r"a|f", s)
if f:
    print("String matches with a or b")
else:
    print("No string match found")


import re
d = "phoneandsims"
f = re.findall(r"p|h", d)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)

d = "phoneandsims"
f = re.findall(r"p|h", d)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)

d = "phoneandsims"
f = re.findall(r"ph|si", d)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)


d = "phoneandsims phoneandsims"
f = re.findall(r"ph|si", d)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)

