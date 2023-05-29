# Tuple is an immutable collection of elements of different data types.
# They are defined by enclosing elements in () parenthesis separated by a comma.


# Empty tuple
tuple = ()
print(tuple)

# String tuple
names  = ('Yash','Sean', 'Siy', 'Gates')
print(names)

# int tuple
numbers = (1,2,3,4)
print(numbers)

#Heterogeneous Tuple
employeeData = (1, "Sean",True,25)
print(employeeData)

#returns the count of the duplicate values in tuples
_student = ("Aditya","DG", "28", "male", "Aditya")
print(_student.count("Aditya"))
print(_student.count("28"))
print(_student.count("male"))