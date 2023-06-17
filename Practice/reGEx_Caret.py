# Caret(^) - Matches the beginning of the string using Pre-fix. Verifies if the string starts with the given characters or not.
# Ex: ^a checks if the string starts with "a" for apple,avacado etc.

import re
d = "abanana, aphone "
a = re.findall(r"^abanana", d)
if a:
    print("There is string matche")
else:
    print("There is no string match")
    print(a)

d = "banana, aphone "
a = re.findall(r"^abanana", d)
if a:
    print("There is string matche")
else:
    print("There is no string match")
    print(a)