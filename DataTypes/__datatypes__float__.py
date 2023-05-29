"""floating point numbers (float) are positive and negative real numbers
 with a fractional part denoted by the decimal symbol . or the scientific notation E or e,
e.g. 1234.56, 3.142, -1.55, 0.23. """

x = 1.2
print(x)
print(type(x))

y = 123_42.222_013
print(y)

""""floating point number can be separated by the underscore _. 
The maximum size of a float is depend on your system.
 The float beyond its maximum size referred as inf, Inf, INFINITY, or infinity. 
For example, a float number 2e400 will be considered as infinity for most systems. """

z = 2e400
print(z)

"""Scientific notation is used as a short representation to express floats having many digits.
 For example: 345.56789 is represented as 3.4556789e2 or 3.4556789E2 """

f = 1e3
print(f)

f = 1e5
print(f)

f = 3.4556789e2
print(f)
print(type(f))

"""*************************** Conversions  ***************************"""
""" float() function to convert string & int to float."""
# syntax is float()

f=float('5.5')
print(f)
print(type(f))

f=float('5')
print(f)
print(type(f))

f=float('-5')
print(f)
print(type(f))

f=float('1e3')
print(f)
print(type(f))

f=float('-Infinity')
print(f)
print(type(f))

f=float('inf')
print(f)
print(type(f))