# Tuple = is a collection  which is ordered and unchangable used to group together related data.
# we use parentheses only.

_student = ("Aditya", "28", "male")
print(_student)

# Functions related to tuples.
# To count duplicates itmes
_student = ("Aditya", "28", "male", "Aditya")
print(_student.count("Aditya"))
print(_student.count("28"))
print(_student.count("male"))



# Tuples are collection which is ordered and unchangable
# Tuples are very similar to list
# We use paraenthyses only.

_furnitures = ("sofa", "table", "chair", "bed", "bed")
print(_furnitures)
print(_furnitures.count("bed"))
print(_furnitures.index("bed"))
print(_furnitures.index("table"))
for x in _furnitures:
    print(x)

    if "sofa" in _furnitures:
        print("sofa i have")
