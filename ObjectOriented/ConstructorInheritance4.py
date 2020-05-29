class A:

    def __init__(self):
        print("In A init")


class B:

    def __init__(self):
        print("In B init")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("In C init")

c = C()