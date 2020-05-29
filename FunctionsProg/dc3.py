def outer_div(func):

    def inner(x,y):
        if(x<y):
           x,y = y,x

        return func(x,y)

    return inner
# syntax of generator
divide1 = outer_div(divide)
divide1(2,4)

@outer_div
def divide(x,y):
    print(x/y)