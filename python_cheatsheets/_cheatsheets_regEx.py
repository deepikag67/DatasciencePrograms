# Caret [ ^ ] - Matches the beginning of the string using Pre-fix. Verifies if the string starts with the given characters or not.

import re
a = "thesun, themoon"
d = re.findall(r"^asun", a)
if d:
    print("There is a string matches")
else:
    print("There is no string matches")

# $ - Dollar - Matches the end of the string i.e suffix.

import re
a = "I am the best in this world007"
d = re.findall(r"ld007$", a)
if d:
    print("There is a string matches")
else:
    print("There is no string matches")

# Asterisk * - Return 0 or more occurrences

import re
a = "IDI/08_SI-(5449)-PR1028886589"
d = re.findall(r"ID.*4", a)
print(d)

a = "IDI/08_SI-(5449)-PR1028886589"
d = re.findall(r"ID.*4*9", a)
print(d)

# Plus + - One or more occurrences
import re
a = "HancockHoldingCOMPANYSBS"
d = re.findall(r"n.+M", a)
print(d)

# Question mark ? - - Return 0 or One occurrences
import re
a = "Passport"
d = re.findall(r"Pa.?s", a)
print(d)

# either or - It acts as an operator.
# # It checks the pattern before or after the "or" symbol present in the string

import re
a = "SingaporeandIndia"
b = re.findall(r"Si|In", a)
print(b)



