# Sets = is a collection which is unordered as well as being unindexed
# They do not allow any duplicates values
# Curly Brackets is used only ({ }).
# Sets are faster than list

phones = {"oppo", "vivo", "samsung", "iphone"}
print(phones)

# To add we use
phones = {"oppo", "vivo", "samsung", "iphone"}
phones.add("karbon")
print(phones)

# To remove we use
phones = {"oppo", "vivo", "samsung", "iphone"}
phones.remove("oppo")
print(phones)

# To clear we use
phones = {"oppo", "vivo", "samsung", "iphone"}
phones.clear()
print(phones)

# To update an elements in sets we use
phones = {"oppo", "vivo", "samsung", "iphone"}
sims = {"airtel", "jio", "vodafone"}
phones.update(sims)

# To check common thing we use
phones = {"oppo", "vivo", "samsung", "iphone", ("jio")}
sims = {"airtel", "jio", "vodafone"}
phones_sims = phones.union(sims)


# Sets are collections which is unordered and unindexed
# They do not allow any duplicates value.
# Curly brackets are used only
# Sets are faster then list

_clothes_brands = {"chanel", "nike", "adidas", "levis"}
print(_clothes_brands)

# To add we use
_clothes_brands = {"chanel", "nike", "adidas", "levis"}
_clothes_brands.add("gucci")
print(_clothes_brands)

# To remove we use
_clothes_brands = {"chanel", "nike", "adidas", "levis"}
_clothes_brands.remove("levis")
print(_clothes_brands)

# To clear all we use
_clothes_brands = {"chanel", "nike", "adidas", "levis"}
_clothes_brands.clear()
print(_clothes_brands)