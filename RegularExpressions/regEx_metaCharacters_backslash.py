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


#\n is prints the string in new line.
# Split the string into new line
s = "Deepika@DESKTOP-V34\nC1IL78787"
print(s)


#\b Returns the right boundary of the string
# Identifies the string with common sequence of characters.
s = "OneNinja OneNinja OneNinja OneNinja OneNinja OneNinja OneNinja OneNinja"
f = re.findall(r'Ninja\b', s)
print(f)


#\B Returns the right boundary of the string
# Return only the part of the string where the string is without spaces.
s = "OneNinjaOneNinja"
f = re.findall(r"Ninja\B", s)
print(f)


#\A -  returns the beginning character of the string but not numbers
s = "Aditya"
f = re.findall(r"\AA", s)
print(f)



# \0 returns null character
s = "\0"
f = re.findall("\0", s)
#print(f)
if f:
    print("Returns null character")
else:
    print("There is no null character")


import re
deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall("\d", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall("\D", deepika)
print(aditya)


deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall("\w", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall("\W", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall("\s", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall("\S", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya\nAnd ADITYA also loves Deepika"
print(deepika)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall(r"loves\b", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall(r"Deepika\b", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall(r"aditya\b", deepika)
print(aditya)


deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall(r"ADITYA\b", deepika)
print(aditya)

deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall(r"Deepika\B", deepika)
print(aditya)



deepika = "DEEPIKA31/01/1988@ loves-24/01/1997aditya. And ADITYA also loves Deepika"
aditya = re.findall(r"\AD", deepika)
print(aditya)