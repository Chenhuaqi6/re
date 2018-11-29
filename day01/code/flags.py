import re
#re.I 忽略大小写
s = "Hello Word"
pattern = r"hello"
regex = re.compile(pattern,re.I)
l = regex.findall(s)
print(l)

#使 . 可以匹配换行
s = """Hello Word
hello Kitty
"""
pattern = r".+"
regex = re.compile(pattern,re.S)
l = regex.findall(s)
print(l)

#使其可以匹配每一行的开头结尾位置
s = """Hello word
hello Kitty
"""
pattern = r"^hello"
#pattern = r"word$"

regex = re.compile(pattern,re.M)
l = regex.findall(s)
print(l)

