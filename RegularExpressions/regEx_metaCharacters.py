# Metacharacters - The syntax contains special characters - [],\,.,^,$,*,(),|,{},+,?
# Each special character identifies the string in different ways.


# Using [] - Square brackets - Return the lower case characters between a and l
import re

s = "Deepika@DESKTOP-V34C1IL"
f = re.findall("[a-l]", s) # lower case
print(f)


# Using \ - Back Slash - Return the digits/numbers in the string
s = "Deepika@DESKTOP-V34C1IL7"
f = re.findall("\d", s)
print(f)


# Using . - dot - Return a specific sequence in a string
s = "Deepika"
f = re.findall("De..a", s)
f = re.findall("De.a", s)
print(f)





