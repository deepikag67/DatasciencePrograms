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



