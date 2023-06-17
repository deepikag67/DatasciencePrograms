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