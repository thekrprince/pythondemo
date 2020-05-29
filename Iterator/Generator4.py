def square():
    n = 1
    while n <= 10:
        sq = n * n
        n += 1
        yield sq


res = square()

for x in res:
    print(x)