class Div:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __truediv__(self, other):
        return self.a/self.b, other.a/other.b


a1 = Div(35, 7)
a2 = Div(21, 4)

print(a1/a2)