'''
    生产者：厨师 3个
    消费者：顾客 6个，每人3000元，若篮子不够，用户等待2秒，继续判断有没有，有的话继续购买，直到钱花完
    蛋挞篮子：500个蛋挞满，当满了，停顿3秒钟，判断篮子是否已满，没满则继续生产，满了则继续等待
    蛋挞的单价是2元
'''
from threading import Thread
import time
tart=500
class Productor(Thread):
    username = ""
    count = 0
    def run(self) -> None:
        global tart
        while True:
            if tart == 500 :
                time.sleep(3)
            elif 0 <= tart < 500:
                tart = tart+1
                self.count=self.count+1
                print(self.username,"做了1个蛋挞,篮子里共",tart,"个蛋挞")
                print(self.username,"一共做了",self.count,"个蛋挞")
            else :
                break

class Customer(Thread):
    usernameC = ""
    countC = 0
    money = 3000
    def run(self) -> None:
        global tart
        while True:
            if 0 < tart <= 500:
                if self.money > 0:
                    tart = tart - 1
                    self.countC = self.countC + 1
                    self.money = self.money - 2
                    print(self.usernameC,"买了",self.countC,"个蛋挞还有",self.money,"元钱")
                elif self.money == 0:
                    print(self.usernameC,"没钱了")
                    break
                else:
                    break
            elif tart == 0 :
                time.sleep(2)
                print("蛋挞没了正在做…………")
            else :
                break


p1=Productor()
p1.username="张三"
p2=Productor()
p2.username="李四"
p3=Productor()
p3.username="王五"

c1=Customer()
c1.usernameC="赵飞燕"

c2=Customer()
c2.usernameC="西施"

c3=Customer()
c3.usernameC="貂蝉"

c4=Customer()
c4.usernameC="王昭君"

c5=Customer()
c5.usernameC="甄宓"

c6=Customer()
c6.usernameC="甄嬛"

p1.start()
p2.start()
p3.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()









