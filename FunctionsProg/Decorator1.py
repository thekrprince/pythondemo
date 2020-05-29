
def div(x, y):
    print(x/y)


def outer_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


divide = outer_div(div)

divide(4, 8)