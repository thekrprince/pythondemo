from threading import *


def table(n):
    for x in range(1, 11):
        print(n * x)


t1 = Thread(target=table, args=(3,))
t1.start()
t1.join()
print("Counting finished")