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

#\n Returns the new line
s = "24/01/1997aditya@loves\n31/01/1988deepika"
print(s)


#\b Returns the boundary of the string
s = "24/01/1997aditya@loves31/01/1988deepika"
f = re.findall(r'aditya\b', s)
print(f)


#\B Returns the boundary of the string
s = aditya@lovesdeepika"
f = re.findall(r"deepika\B", s)
print(f)


#\A -  returns the beginning character of the string
s = "OneNinja"
f = re.findall(r"\AO", s)
print(f)