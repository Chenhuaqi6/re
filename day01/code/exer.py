import re
f = open("test.txt")
data = f.read()
pattern = r"\b[A-Z]\S*" #大写字母开头的
pattern = r"-?\d+\.?/?\d*%?" #匹配任意小数 分数 负数
regex = re.compile(pattern)
l = regex.findall(data)
print(l)