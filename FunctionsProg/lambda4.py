from functools import *

num = [12, 6, 43, 19, 6, 4]

sum = reduce(lambda a, b: a+b, num)

print(sum)