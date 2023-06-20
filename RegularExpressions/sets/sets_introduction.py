# Set of characters inside a [] brackets with a special meaning.

import re

# Return the match of the specified characters inside the [].
# Ex: Pythonn11 - [yon1] - returns [y,o,n,n,1,1]
# Returns alphanumeric
# Return all occurrences
s = "IDI/08_AI-(5449)-PR98042"
f = re.findall("[5ID]", s)
print(f)


# Return a match for any lower case character only
# Does not return Upper case character
s = "idi/08_AI-(5449)-id98042z"
f = re.findall("[a-z]", s)
print(f)

# Does not return match for characters mentioned in square brackets
s = "Idi/08_AI-(5449)-id98042z"
f = re.findall("[^i]", s)
print(f)


# Returns the match for the specified digits in the string
# Returns all the occurrences
s = "Idi/08_AI-(5449)-id98042z"
f = re.findall("[09]", s)
print(f)


# Returns a match for any digit between 0 and 9
s = "Idi/08_AI-(5449)-id98042z"
f = re.findall("[0-9]", s)
print(f)

# Returns a match between any two digit numbers 00 and 59
s = "Idi/08_AI-(5449)-id98042z"
f = re.findall("[0-5][0-9]", s)
print(f)

# Returns a match for any character alphabetically between a and z
# It can be a lower case or upper case
s = "Idi/08_AI-(5449)-id98042z"
f = re.findall("[a-zA-Z]", s)
print(f)


# Returns a match for a string with any special character character
s = "Idi/08_AI-(54+49)-id9*8$+042z"
f = re.findall("[+]", s)
g = re.findall("[*]", s)
h = re.findall("[$]", s)
print(f)
print(g)
print(h)



