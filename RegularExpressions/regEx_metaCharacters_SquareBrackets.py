# Metacharacters - The syntax contains special characters - [],\,.,^,$,*,(),|,{},+,?
# Each special character identifies the string in different ways.


# Using [] - Square brackets - Return the lower case characters between a and l
import re
s = "Deepika@DESKTOP-V34C1IL"
f = re.findall("[a-l]", s) # lower case
print(f)

# Using [] - Square brackets - Return the upper case characters between a and l
import re
s = "Deepika@DESKTOP-V34C1IL"
f = re.findall("[A-Z]", s) # Upper case
print(f)

# Using [] - Square brackets - Return the digits\numbers from 0 to 9
import re
s = "Deepika@DESKTOP-V34C1IL"
f = re.findall("[0-9]", s) # digits
print(f)




