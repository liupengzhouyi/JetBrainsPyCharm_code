#usr/bin/python3.6
#coding: UTF-8
#fileName: HotDog.py

class HotDog:
    def __init__(self, monny, kg, time):
        self.monny = monny
        self.kg = kg
        self.time = time

    def __str__(self):
        str = "这个hotdog买" + self.monny + "元，重量：" + self.kg + "Kg, 生产日期：" + self.time + "."
        return str

