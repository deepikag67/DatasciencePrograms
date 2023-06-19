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

# Using [] - Square brackets - Return the lower case characters between a and z
import re
f = "ghpq9jFrva_eVh8Nr9s9c4PBlgIVfZqTOe2zmp2d"
r = re.findall("[a-z, [0-9]", f)
print(r)

# Using [] - Square brackets - Return the upper case characters between a and l
import re
f = "DEEPIKA31/01/1988 LOVES ADITYA VERY MUCH AND ADITYA24/01/1997. NOTHING CAN SEPARATE THEM FROM EACH OTHER. WE ARE FUCKING IN LOVE WITH EACH OTHER"
R = re.findall("[A-z, [0-9]", f)
print(R)




