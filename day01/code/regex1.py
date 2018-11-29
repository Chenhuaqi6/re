import re

s = "2008年发生了很多大事,08奥运,512地震等"
# s = "zhang:1994 li:1993"
pattern = r"\d+"

# l = re.findall(pattern,s)
# print(l)
regex = re.compile(pattern)
l = regex.findall(s,0,18)
print(l)

