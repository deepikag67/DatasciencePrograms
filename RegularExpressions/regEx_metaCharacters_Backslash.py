# Metacharacters - The syntax contains special characters - [],\,.,^,$,*,(),|,{},+,?
# Each special character identifies the string in different ways.


# Using \ - Back Slash - Return the digits/numbers in the string
#\d -returns the numbers from 0 to 9
import re
s = "Deepika@DESKTOP-V34C1IL7"
f = re.findall("\d", s)
print(f)

#\D - returns the non decimal digits i.e alphabets and special characters
s = "Deepika@DESKTOP-V34C1IL7"
f = re.findall("\D", s)
print(f)

#\s - Returns white space characters
s = "Deepika@ DESKTO P-V34C 1IL7"
f = re.findall("\s", s)
print(f)

#\S- Returns non white space characters i.e returns only alphanumeric and special characters
s = "Hello World1@"
f = re.findall("\S", s)
print(f)

#\w - Returns the alphanumeric but not the special characters
s = "Deepika@DESKTOP-V34C1IL78787"
f = re.findall("\w", s)
print(f)

# \W - Returns the special characters but not alphanumeric
s = "Deepika@DESKTOP-V34C1IL78787"
f = re.findall("\W", s)
print(f)



#\n Returns the new line
s = "Deepika@DESKTOP-V34\nC1IL78787"
print(s)


#\b Returns the boundary of the string
s = "One Ninja"
f = re.findall(r'One\b', s)
print(f)


#\b Returns the boundary of the string
s = "OneNinja"
f = re.findall(r"One\B", s)
print(f)


#\A -  returns the beginning character of the string
s = "OneNinja"
f = re.findall(r"\AO", s)
print(f)



# \0 returns null character
s = "0Deepika@DESK TOP-V34C1I L78787"
f = re.findall("\0", s)
print(f)






