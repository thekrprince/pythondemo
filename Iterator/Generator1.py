def fun():

    yield 1
    yield 2
    yield 3


res = fun()
print(res.__next__())
print(res.__next__())
print(res.__next__())