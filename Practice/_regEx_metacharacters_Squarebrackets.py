# Metacharacters - The syntax contains special characters - [],\,.,^,$,*,(),|,{},+,?
# Each special character identifies the string in different ways.

# Using [] - Square brackets - Return the lower case characters between a and l
import re
d = "24/01/1997Aditya@loves31/01/1988Deepika"
a = re.findall("[a-l]", d)
print(a)

# Using [] - Square brackets - Return the upper case characters between a and l
d = "24/01/1997Aditya@loves31/01/1988Deepika"
a = re.findall("[A-Z]", d)
print(a)

# Using [] - Square brackets - Return the digits\numbers from 0 to 9
d = "24/01/1997Aditya@loves31/01/1988Deepika"
a = re.findall("[0-9]", d)
print(a)