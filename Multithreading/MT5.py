from threading import *


class EX:

    def A(self):
        lst = ['God', 23, 56.99, 'K', 10]
        for ele in lst:
            print(ele)


obj = EX()

t1 = Thread(target=obj.A())
t1.start()
t1.join()
print("Done")