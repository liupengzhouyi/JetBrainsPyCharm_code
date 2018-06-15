#usr/bin/python3.6
#coding: UTF-8
#fileName: splitString.py

#分解
name = "sun,eclipse,idea,vs,unity,e"
names = name.split(',')
for i in names:
    print(i)

#连接
tempName = ','.join(names)
print(tempName)



