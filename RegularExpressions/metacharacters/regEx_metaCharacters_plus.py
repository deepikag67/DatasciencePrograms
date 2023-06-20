# Plus + - One or more occurrences

# Concatination of the characters
import re
empId = "AD001STAQ"
f = re.findall("AD.+S", empId)
print(f)


empId = "AD001STIP"
f = re.findall("AD.+S", empId)
print(f)

import re
IFSCcode = "UBIN056681"
f = re.findall("UB.+1", IFSCcode)
print(f)

IFSCcode = "UBIN056681007"
f = re.findall("UB.+1*7", IFSCcode)
print(f)





