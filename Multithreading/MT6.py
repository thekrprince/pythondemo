from threading import *
from time import sleep


class Even:

    def __init__(self, num):
        self.num = num

    def even(self):
        for i in range(1, self.num+1):
            if i % 2 == 0:
                print("Even - ", i)
                sleep(1)


class Odd:

    def __init__(self, num):
        self.num = num

    def odd(self):
        for i in range(1, self.num+1):
            if i % 2 == 1:
                print("Odd - ", i)
                sleep(1)


n = 30
obj1 = Even(n)
obj2 = Odd(n)

t1 = Thread(target=obj1.even())
t2 = Thread(target=obj2.odd())

t1.start()
sleep(0.1)
t2.start()