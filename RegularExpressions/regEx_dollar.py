# $ - Dollar - Matches the end of the string i.e suffix.
# Verifies if the string ends with a certain character

# Ex: If the strings banana ends with a

import re
s = "orange"
f = re.findall(r"nge$", s)
if f:
    print("String match found")
else:
    print("String Match not found")