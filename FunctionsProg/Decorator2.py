def outer_div(func):

    def inner(x, y):
        if x < y:
            x, y = y, x
        return inner(x, y)

    return inner

@outer_div
def div(x, y):
    print(x/y)