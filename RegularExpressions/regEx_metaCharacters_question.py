# Question mark ? - - Return 0 or more occurrences

import re
empId = "AD00S01"
f = re.findall("AD00.?S", empId)
print(f)


import re
empId = "AD00S20000"
f = re.findall("AD00.?S", empId)
print(f)


# Using Question mark & Asterisk

import re
empId = "AD00S01K"
f = re.findall("AD00.?S.*K", empId)
print(f)


import re
empId = "AD00S20000K"
f = re.findall("AD00.?S.*K", empId)
print(f)


import re
empId = "AD00L01K"
f = re.findall("AD00.?L.*K", empId)
print(f)


import re
empId = "AD00L20000K"
f = re.findall("AD00.?L.*K", empId)
print(f)

Ifsccode = "UBIN051748936975"
f = re.findall("UB.?I", Ifsccode)
print(f)

Ifsccode = "UBIN051748936975"
f = re.findall("UB.?I.*4", Ifsccode)
print(f)

Ifsccode = "UBIN051748936975"
f = re.findall("UB.?I.*4.?8", Ifsccode)
print(f)

Ifsccode = "UBIN051748936975"
f = re.findall("UB.?I.*4.?8.*5", Ifsccode)
print(f)