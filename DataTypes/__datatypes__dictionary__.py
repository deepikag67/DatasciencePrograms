# Dictionary is an unordered collection that contains key:value pairs separated by commas inside curly brackets.


countryCapitals = {"India" : "Delhi", "France" : "Paris"}
print(countryCapitals)
countryCapitals.update({"Singapore" : "Singapore"})
print(countryCapitals)


countryCapitals = {'India' : 'Delhi', 'France' : 'Paris'}
print(countryCapitals)

# Empty Dictionary

dict = {}
print(dict)

# int key string value
dict = {1:"Key",2:"Value",3: 'Deepika'}
print(dict)

# string key int value
dict = {"Key" : 1, "Value" : 2}
print(dict)

# float key and string value
dict = {1.6 : "one", 5.6 : "five"}
print(dict)

# tuple key and string value
dict = {("python","java","c++"): "Programminglanguages",("jira","confluence","wiki") : "Tools"}
print(dict)

#string key list value
dict = {"fruits":["Apple","Orange"],"colors" : ["Pink","Blue"]}
print(dict)

