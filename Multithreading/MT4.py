from threading import *
from time import sleep


class Square(Thread):

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        for i in range(1, self.num+1):
            res = i * i
            print("Square of {} is {}".format(i, res))
            sleep(1)


class Cube(Thread):

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        for i in range(1, self.num + 1):
            res = i * i * i
            print("Cube of {} is {}".format(i, res))
            sleep(1)


n = 5
sq = Square(n)
cu = Cube(n)

sq.start()
sleep(0.1)
cu.start()

sq.join()
cu.join()
print("Loop Ended!!! Bye")