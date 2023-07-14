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


# To define a function that take two integers
# and return the sum of those two numbers
def add(a, b):
    return a + b

z = "This is a String with special characters !@#$%^&&&&&()()()()"
x = re.findall("[&]", z)  # Used Square brackets
print(x)


z = "This is a string\nThis is a string"
#x = re.findall("\n") # Backslash
print(z)

# Identify the numbers in the string - \d
# Identify the alphabets & special characters together in a string - \D
# Identify the empty spaces in a string - \s
#


sourcefile = open("C://Technology//DevOps//Steps//aditya.txt", "w")
print("Hello", file=sourcefile)
sourcefile.close()


with open("C://Technology//DevOps//Steps//aditya.txt", "w") as file:
    file.write('Hello World!')


# initializing the variables
num1 = 10
num2 = 5

# function calling and store the result into sum_of_twonumbers
sum_of_twonumbers = add(num1, num2)

# To print the result
print("Sum of {0} and {1} is {2};".format(num1,num2, sum_of_twonumbers))


print("Hello ", " World", sep='***')

print("I'm below two lines")

# code for disabling the softspace feature
print('G','F','G')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')


#print('Hello','World',end='!!!')


print('Hello.','How are you?')


# Numbers
print(1)
# Lists
print([1, 2, 3])
# Dictionaries
print({'name': 'John', 'age': 36})
# Booleans
print(True)
# None
print(None)
# Strings
print("Hello, World")
# Touple
print((1, 2, 3))
# Sets
print({1, 2, 3})

#print("Welcome to", end = ' ')
#print("GeeksforGeeks", end= ' ')

print("Hello world")
print("Welcome to Python")


print("Hello world!", end =" ")
print("Welcome to Python")


print("Python", end ="@")
print("Home")


#sourceFile = open('c://users//Documents//python.txt', 'r')
#print('Hello, Python!', file = sourceFile)
#sourceFile.close()







from time import sleep

#output is not flushed here
#print("Hello, world!", end='')
#sleep(5)
#print("Bye!!!")


from time import sleep

# output is flushed here
#print("Hello, world!", end='', flush= True)
#sleep(5)
#print("Bye!!!")

print("This output will be flushed immediately", flush=True)


import keyword
print(keyword.kwlist)


#checking length
print(f"Total number of keywords: {len(keyword.kwlist)}")

#1 import
import math
print("factorial of 5 is :", math.factorial(5))

#2 elif
# Code using elif keyword
a = 5
if a > 5:
    print("a is greater than 5")
elif a == 5:
    print("a is equal to 5")
else:
    print("a is less than 5")

#3 else
# Code using else keyword
num = 100
if num < 1:
    print("Number is less than 1")
elif num < 10:
    print("Number is less than 10")
else:
    print("Number is greater than or equal to 100")

#4 If keyword
#Code using if keyword
a = 10
if a > 5:
    print("a is greater than 5")

#5 In Keyword
# Code to check 'in' keyword using list
a = 10
b = [10, 20, 30]
c = "10"
print(a in b)  # True
print(c in b)  # False
# Code to check 'in' keyword using string
name = "John"
print("J" in name)  # True
print("b" in name)  # False

#6 Is Keyword
# Code to check 'is' keyword
a = 10
b = 10
c = "10"
print(a is b)  # True
print(a is c)  # False
print(a is not c)  # True

#7 pass keyword
def message():
    pass
class Person:
    pass

#7 with keyword
# using with keyword

#with open("C://Technology//python.txt", "w") as file:
 #file.write("Hello World!")

# 8 yield keyword
# using yield keyword
def nameslist():
     yield "John"
     yield "Sara"
     yield "Mike"
     yield "Molly"
names = nameslist()
# using next() function to get the next value
print(next(names))  # John
print(next(names))  # Sara
print(next(names))  # Mike
print(next(names))  # Molly

# 9 true value
# Code to check 'True' keyword
if True:
    print("True")
    print("----")

print(bool(10)) # True



# 10 false value
# Code to check 'false' keyword
if True:
    print("False")

print(bool()) # False
print(bool()) # False
print(bool([])) # False
print(bool({})) # False
print(bool(None))# False


# Local variable

def greet():
    # local variable
    message = 'Hello'
    print('Local', message)
greet()
# try to access message variable
# outside greet() function
print(message)


# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)


# outside function
def outer():
    message = 'local'

    # nested function
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

