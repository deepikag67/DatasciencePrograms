"""Deepika Guduru v1.0
Numbers or integers
An integer can be a 0 (Zero), 100(positive number) and -10(Negative numbers)
Snake case Variable declaration
using multiline comment"""
_integer_zero1 = 0
print(_integer_zero1)
_integer_positive = 100
print(_integer_positive)
_integer_negative = -10
print(_integer_negative)

"""An integer can be 0b11011000 (binary), 0o12 (octal) and 0x12 (hexadecimal) values
"""
_integer_binary = 0b10110111
print(_integer_binary)
_integer_octal = 0o12
print(_integer_octal)
_integer_hexadecimal = 0x12
print(_integer_hexadecimal)


"""Leading zeros in non-zero integers are not allowed
Pascal Case Variable declaration"""
IntLeadingZero = 123456
intleadingzero = 23456
print(IntLeadingZero)
print(intleadingzero)


"""Python does not allow comma as number delimiter. Use underscore _ as a delimiter instead
Camel case variable declaration"""
intUnderscore = 1_234_567_89
print(intUnderscore)


"""Integers must be without a fractional part (decimal point).
 It includes a fractional then it becomes a float. """
# Syntax - type()
intfloatingnum = 5.0
print(type(intfloatingnum))



"""Binary
A number having 0b with eight digits in the combination of 0 and 1 represent the binary numbers in Python.
For example, 0b11011000 is a binary number equivalent to integer 216."""
x = 0b11011000
print(x)
x = 0b_1101_1000
print(x)
print(type(x))


"""*************************** Conversions  ***************************"""
"""int converts a string or a float into an integer"""
# Strings
name = 'Deepika'
print(name)
print(type(name))

# syntax - int()
x = int('100')
print(x)
print(type(x))

y = int('-10')
print(y)
print(type(y))

z = int(5.5)
print(z)
print(type(z))


