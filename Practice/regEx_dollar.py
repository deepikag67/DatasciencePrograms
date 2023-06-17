# $ - Dollar - Matches the end of the string i.e suffix.
# Verifies if the string ends with a certain character
import re

# Ex: If the strings banana ends with a

a = "DEEPIKA"
d = re.findall(r"PIKA$", a)
if d:
    print("There is a string match found")
else:
    print("There is no string match found")
    print(d)

a = "DEEPIKA"
d = re.findall(r"pika$", a)
if d:
    print("There is a string match found")
else:
    print("There is no string match found")
    print(d)