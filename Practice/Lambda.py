# Lambda program practice
from functools import *

# Single Argument
x = lambda a: a+10

print(x(10))

# Multiple Argument
y = lambda a, b, c: a*b*c

print(y(2, 3, 4))

# filter function
lst = [4, 5, 7, 8, 12, 17]
odd = list(filter(lambda a: (a % 2 != 0), lst))
print(odd)

# map function
mul = list(map(lambda a: a*2, lst))
print(mul)

# reduce function
mul1 = reduce(lambda a, b: a*b, lst)
print(mul1)