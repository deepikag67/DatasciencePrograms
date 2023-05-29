"""

(1) Definition of Function:
It performs a task which is re-usable contains block of programming statements
The keyword is 'def'
"""

# Functions can store variables, pass parameters, return function, store data in data structures such as
# hash, tuples, lists, dict....

#Syntax
# def function_name(parameters/Arguments) :
#     """Write String"""
#     statement1
#     statement2
#     statement3
#     ...
#     return [expr]


# Calculator that returns only one value
def calculator(a,b):
    """Calculator"""
    add = a+b
    sub = a-b
    return sub
res = calculator(12,6)
print("Substraction :", res)



# Calculator that returns multiple values
def calculator(a,b):
    """Calculator"""
    add = a+b
    sub = a-b
    return sub,add
res = calculator(12,6)
print("calculator :", res)



# Printing string
# Return keyword returns the output of the function
def username(str) :
    """Printing name"""
    user = str
    return user;
res = username("Deepika")
print(res)


# define a function that returns a Dictionary
def capitals(a1,a2,a3) :
    countryCapitals = {'India': a1, 'France': a2, 'Singapore': a3}
    return countryCapitals

res = capitals("Delhi","UK","SG")
print(res)


# define a function that returns a tuple
def colors(x1,x2,x3) :
    colourcode = (x1, x2, x3)
    return colourcode

res = colors("pink","red","black")
print(res)


# define a function that returns a list
# define a function that returns a sets





# Define python function using Positional arguments
def bike(name,model):
    print(name) # statements
    print(model)
#Calling functions
bike("Yamaha","12387")


# Define python function using Keyword arguments
def bike(name, model):
    print(name)  # statements
    print(model)

#Calling function
bike(name = "Yamaha", model = "S12387")


# default args

# Optional args
def calendar(year, month, date =''):
    print(year,month,date)

#   Calling function
calendar(2023,5)

# Passing arbitrary number of arguments to a function
def colors(*colorcode) :
    print(colorcode)

# Calling Function
colors("pink","blue","orange")
colors("red","white")

# Nested Functions
def function1() :
    p = "Hello World"
    def function2() :
        print(p)
        # Calling function 2
        function2()
# Calling function 1
function1()


