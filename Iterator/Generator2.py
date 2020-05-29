def fun():

    yield 1
    yield 2
    yield 3
    yield 4


for val in fun():
    print(val)