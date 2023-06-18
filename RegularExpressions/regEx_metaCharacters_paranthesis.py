# groups the sub pattern


import re
s = "axb avc cfda"
f = re.findall(r"(a)", s)
print(f)
if f:
    print("String matches with a or b")
else:
    print("No string match found")


import re
s = "abcd"
f = re.findall(r"(abc)", s)
print(f)
if f:
    print("String matches with a or b")
else:
    print("No string match found")


import re
s = "gacd"
f = re.findall(r"(cd)", s)
print(f)
if f:
    print("String matches with a or b")
else:
    print("No string match found")

import re
deepika = "adityaanddeppika"
f = re.findall(r"(ad)", deepika)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)

import re
deepika = "adityaanddeppika"
f = re.findall(r"(de)", deepika)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)

import re
deepika = "adityaanddeppika"
f = re.findall(r"(adka)", deepika)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)

import re
deepika = "adityaanddeepika"
f = re.findall(r"(ddeepika)", deepika)
if f:
    print("String matches with a or b")
else:
    print("No string match found")
print(f)