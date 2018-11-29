import re
pattern = r"(ab)cd(?P<dog>ef)"

regex = re.compile(pattern)

obj = regex.search("abcdefghi")
# print(obj.group())

#属性
print(obj.pos) #目标字串开始位置
print(obj.endpos) #目标字串结束位置
print(obj.re)  #正则表达式
print(obj.string) #目标字符串
print(obj.lastgroup) #最后一组组名
print(obj.lastindex) #最后一组序列号
print("===============================")

print(obj.start()) #匹配内容的开始位置
print(obj.end())  #匹配内容的结束位置
print(obj.span()) #匹配内容的起止位置
print(obj.group("dog"))
print(obj.group("dog"))
print(obj.group("dog"))