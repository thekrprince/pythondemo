from threading import *
from time import sleep


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


h1 = Hi()
h2 = Hello()

h1.start()
sleep(0.1)
h2.start()

h1.join()
h1.join()

print("Bye")