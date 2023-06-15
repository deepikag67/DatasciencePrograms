# Metacharacters - The syntax contains special characters - [],\,.,^,$,*,(),|,{},+,?
# Each special character identifies the string in different ways.

#Using \ - Back Slash - Return the digits/numbers in the string
#\d -returns the numbers from 0 to 9

import re
c = "24aditya01@loves31deepika01"
f = re.findall("\d", c)
print(f)

#\D - returns the non decimal digits i.e alphabets and special characters
c = "24aditya01@loves31deepika01"
f = re.findall("\D", c)
print(f)

#\s - Returns white space characters
c = "24/01/1997 aditya @ loves 31/01/1988 deepika"
f = re.findall("\s", c)
print(f)

#\S- Returns non white space characters i.e returns only alphanumeric and special characters
c = "24/01/1997 aditya @ loves 31/01/1988 deepika"
f = re.findall("\S", c)
print(f)

#\w - Returns the alphanumeric but not the special characters
c = "24aditya01@loves31deepika01"
f = re.findall("\w", c)
print(f)

# \W - Returns the special characters but not alphanumeric
c = "24/01/1997 aditya @ loves 31/01/1988 deepika"
f = re.findall("\W", c)
print(f)
