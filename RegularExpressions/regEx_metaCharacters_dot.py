# Returns the number of dots in the string
import re
s = "Python is not a snake.Python is a programming language. It is a high level language."
f = re.findall(r"\.", s)
print(f)



