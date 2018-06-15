#usr/bin/python3.6
#coding: UTF-8
#fileNmae: paly.py

numbers = range(0,13)
kind = ('♥', '♠', '♣', '♦')

allNumber = []
allNumber01 ={}

A = []
B = []
C = []
D = []
E = []

used = []

for i in numbers:
    for j in kind:
        tempNumber = j + (i+1).__str__()
        allNumber.append(tempNumber)
num = 1
for i in allNumber:
    allNumber01[num] = i
    print(i, num)
    num = num + 1

allNumber01[53] = "小妖"
allNumber01[54] = "大妖"

for i in range(1, 55):
    print(allNumber01[i])
num = 0
while(num < 55):
    A.append(allNumber01[num])
    num = num + 1
    B.append(allNumber01[num])
    num = num + 1
    C.append(allNumber01[num])
    num = num + 1
    D.append(allNumber01[num])
    num = num + 1
    E.append(allNumber01[num])

for i in A:
    print(i)




