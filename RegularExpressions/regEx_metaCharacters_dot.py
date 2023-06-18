# Returns the number of dots in the string
import re
s = "Python is not a snake.Python is a programming language. It is a high level language."
f = re.findall(r"\.", s)
print(f)

import re
g = "She is best for me. I love her endlessly. I cant live without her. Because of me she got upset today. I am only afraid to lose her."
d = re.findall(r"\.", g)
print(d)


