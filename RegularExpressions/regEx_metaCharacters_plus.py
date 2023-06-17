# Plus + - One or more occurrences

# Concatination of the characters
import re
empId = "AD001STAQ"
f = re.findall("AD.+S", empId)
print(f)


empId = "AD001STIP"
f = re.findall("AD.+S", empId)
print(f)






