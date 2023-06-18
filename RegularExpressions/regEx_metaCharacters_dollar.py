# $ - Dollar - Matches the end of the string i.e suffix.
# Verifies if the string ends with a certain character

# Ex: If the strings banana ends with a

import re
s = "orange1"
f = re.findall(r"nge1$", s)
print(f)
if f:
    print("String match found")
else:
    print("String Match not found")

