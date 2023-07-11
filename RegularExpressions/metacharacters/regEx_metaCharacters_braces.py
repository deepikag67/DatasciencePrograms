# Braces {} - matches the string specified

#Midd
import re
s = "Aditya"
f = re.findall(r"Adi.{2}a", s)
print(f)


s = "Aditya123"
f = re.findall(r"Aditya.{3}", s)
print(f)


s = "Deepika"
f = re.findall(r".{3}pika", s)
print(f)

s = "Adityalovesdeepika"
f = re.findall(r"A.{17}", s)
print(f)

s = "Adityalovesdeepika"
f = re.findall(r"l.{11}", s)
print(f)

s = "Adityalovesdeepika"
f = re.findall(r"A.{5}", s)
print(f)

s = "Adityalovesdeepika"
f = re.findall(r"l.{6}", s)
print(f)

This