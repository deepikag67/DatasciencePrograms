# List = is used to store multiple items in a single variable
# we use square brackets only ([ ]) and comma to separate items.
emotions = ["aditya","loves","deepika"]
print(emotions)

# For indexing in list
emotions = ["aditya","loves","deepika"]
print(emotions[2])
print(emotions[1])
print(emotions[0])

# We can update or can make changes
emotions = ["aditya","love","deepika"]
emotions [0] = "i"
print(emotions [0])

# To get all together after changing
emotions = ["aditya","love","deepika"]
emotions [0] = "i"

# To add many list in list we use
emotions = ["aditya","love","deepika"]
love = ["deepika","love","aditya"]
character = ["me","only","love","deepika"]
_aditya_deepika = [emotions,love,character]
print(_aditya_deepika)
print(_aditya_deepika[0][2])
print(_aditya_deepika[1][1])
print(_aditya_deepika[2][0])

# To add in list we use
emotions = ["aditya","love","deepika"]
emotions.append("adi")

# List Practice again
# List is used to store multiple items in a string variable
# We use square brackets in list [ ].
# List is mutable we can change anything in it.

_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
print(_cars)

# How we do indexing in list
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
print(_cars [0])
print(_cars [4])
print(_cars [-4])
print(_cars [-3])

# We can update in list thats why it called mutable
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars [-1] = "ranger rover"
print(_cars[-1])

# To get all together or loop after changing in element
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars [-1] = "ranger rover"
for x in _cars:
    print(x)

# To add many list all together
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars2 = ["bmw", "audi", "jaguar"]
_cars3 = ["harrier", "honda city", "mg hector", "baleno"]
_total_cars = [_cars,_cars2,_cars3]
print(_total_cars)

# To add something we use
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars.append("swift")
print(_cars)

# TO remove we use
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars.remove("roll royce")
print(_cars)

# To reomove last item
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars.pop()
print(_cars)

# To insert other thing we use
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars.insert(4,"lamborgini")
_cars.insert(2,"thar")
print(_cars)

#
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars.sort()
print(_cars)

# To clear all things in list we use
_cars = ["porch", "ferrari", "bently", "roll royce", "bmw"]
_cars.clear()
print(_cars)


# 2D list uses or mutli list
_mnc = ["google", "microsoft", "tata"]
_mnc2 = ["reliance", "infosys", "apple"]
_mnc3 = ["amazon", "flipkart", "boat"]
_all_mncs = [_mnc,_mnc2,_mnc3]
print(_all_mncs)
print(_all_mncs[0])
print(_all_mncs[1])
print(_all_mncs[2])
print(_all_mncs[1][1])
print(_all_mncs[1][0])
print(_all_mncs[1][2])