# usr/bin/python3.6
# coding: UTF-8
# fileName: domoon01.py

print("asd")

# 制表符
print("a\ta")

print("Number \tSquare \tCube")
for i in range(1, 11):
    print(i, '\t', i ** 2, '\t', i ** 3)

# 格式化
name = "liuPeng"
age = 22
print("I am %s and i was years ord!" %name)

#数字
number = 12.345678
print("%.2f" % number)
print("%.3f" % number)
print(number)
print("%i" % number)

#E e记忆法
number = 12.45698
print("%.3e" % number)
print("%e" % number)

#多个格式化
a = "123"
b = 125

print("%s and %d" % (a, b))


c = 'wazsexdrtgybhuji'
longth = c.__sizeof__()
print(longth)
