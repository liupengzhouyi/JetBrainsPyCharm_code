#!/usr/bin/python3
#Coding: -*- UTF-8 -*-
#author: Liupeng

print("Hello World!")

num1 = float(input("请输入一个数字: "))
num2 = float(input("请输入另一个数字: "))

print(num1, num2)

number = int(input("猜数字: "))

if number == 1 :
    print("number = 1")
elif number > 3 :
    if number < 9 :
        pass
    else:
        print("number > 3")
elif number < 9 :
    print("number < 9")
