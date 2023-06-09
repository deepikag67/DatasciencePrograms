# string = is a series of characters to create a string we can either use single or double quotes (',").

name = "MS Dhoni"
print(name)

#  we can add string variable with another string
print("hello i am here "+ name)

# we can check the data type and lenght of variable
print(type(name))
print(len(name))

# we can combine many string
_first_name = "MS"
_last_name = "Dhoni"
_full_name = _first_name + _last_name
print("hi i am aditya ur big fan "  +  _full_name)

_wife_name = 'Shakshi Singh Dhoni'
print(_wife_name   +   "is wife of" , _full_name)

_item_name = "cup"
_item_name2 = "plate"
_combine_items = _item_name + _item_name2
print("we use " + _combine_items)

_phone_name = "vivo"
_sim_name = "jio"
_product_name = _phone_name + _sim_name
print("i have " + _product_name)

_husband_name = "Aditya"
_wife_name = "Deepika"
_couple_name = _husband_name + _wife_name
print("we are couple " + _couple_name)