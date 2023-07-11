# Asterisk * - Return 0 or more occurrences

#Assume there are 20,000 employees
#Requrire to return all the 20,000 employee ID's.
import re
empId = "AD001TA AD002TA AD003TA AD0020000TA "
f = re.findall("AD.*T", empId)
print(f)


empId = "AD20000T"
f = re.findall("AD.*T", empId)
print(f)

Ifsccode = "UBIN0517489"
f = re.findall("UB.*9", Ifsccode)
print(f)

Ifsccode = "UBIN051748936975"
f = re.findall("UB.*I*5", Ifsccode)
print(f)

Ifsccode = "UBIN051748936975145879635"
f = re.findall("UB.*I*5*3.+5", Ifsccode)
print(f)







