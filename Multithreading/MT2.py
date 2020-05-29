from threading import *


def new():
    for x in range(6):
        print("Child Executing", current_thread().getName())


t1 = Thread(target=new)
t1.start()
t1.join()
print("Bye", current_thread().getName())