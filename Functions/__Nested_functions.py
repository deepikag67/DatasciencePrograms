# Nested functions are also called as inner/outer functions
# Inner function : Write a function inside another function
# Access variables within the inner function
# These variables can be public, private and protected(Encapsulation).



# nested function ( INNER)

def outerfun(a1):
    a1 = "outer"

    def innerfun():
        print(a1)

        outerfun("Hello World")



# accessing variables of nested functions

def f1():
    a = "Hello World"

    def f2():
        b = "Pyton"
        print(a)

    f2()
    print(a)






