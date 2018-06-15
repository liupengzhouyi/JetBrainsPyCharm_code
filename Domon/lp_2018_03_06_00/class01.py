#usr/bin/python3
#coding: UTF-8
#fileName: class01.py

class Ball:

    def bounce(self):
        if self.direction == "dowp":
            self.direction = "up"

    def print(self):
        print(self.direction)

myBall = Ball()
myBall.direction = "dowp"
myBall.print()
myBall.bounce()
myBall.print()


