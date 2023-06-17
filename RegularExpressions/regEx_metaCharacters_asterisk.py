# Asterisk * - Return 0 or more occurrences

#Assume there are 20,000 employees
#Requrire to return all the 20,000 employee ID's.
import re
empId = "AD001T"
f = re.findall("AD.*T", empId)
print(f)


empId = "AD20000T"
f = re.findall("AD.*T", empId)
print(f)






