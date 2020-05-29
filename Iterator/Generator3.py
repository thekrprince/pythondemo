def fibonacci(limit):

    a, b = 0, 1

    while a <= limit:
        yield a
        a, b = b, a + b


res = fibonacci(5)

# Iterating over the generator object using next
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())

# Using for in loop
for x in res:
    print(x)