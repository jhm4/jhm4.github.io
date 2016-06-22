import re

a = "my mother is my mom"

b = re.sub('\my', "your", a)

print(b)

c = a.replace(" ", "")

print(c)