#usr/bin/python3.6
#coding: UTF-8
#fileName: domon.py

my_file = open('test.txt', 'a')
#lines = my_file.readlines()
#print(lines)
my_file.write("\n")

my_file.write("abcdefg")

string = input("请输入：")
my_file.write(string)


my_file.close()
