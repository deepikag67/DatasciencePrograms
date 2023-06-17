# It acts as an operator.
# It checks the pattern before or after the "or" symbol present in the string
# a|b matches any string containing a or b such as axb, adb

import re
#a = "deepikaxaditya"
#d = re.findall(r"a|f", a)
#if d:
    #print("String matches with deepika or aditya")
#else:
   # print("No string match found")
   # print(d)

a = "deepxloves"
d = re.findall(r"a|f", a)
if d:
    print("String matches with deepika or aditya")
else:
    print("No string match found")
    print(d)