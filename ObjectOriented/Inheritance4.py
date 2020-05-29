class A:

    def __init__(self):
        print("In A init")

    def feature(self):
        print("Feature 1-A working")


class B:

    def __init__(self):
        print("In B init")

    def feature(self):
        print("Feature 1-B working")


class C(B, A):

    def __init__(self):
        print("In C init")

    def feature1(self):
        print("Feature working")


c = C()
c.feature()