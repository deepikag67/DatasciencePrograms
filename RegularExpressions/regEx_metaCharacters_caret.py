# Caret(^) - Matches the beginning of the string using Pre-fix. Verifies if the string starts with the given characters or not.
# Ex: ^a checks if the string starts with "a" for apple,avacado etc.


import re
s = "anapple anorange"
f = re.findall(r"^anapple", s)
if f:
    print("There is a string match")
else:
    print("There is no string match")
print(f)

