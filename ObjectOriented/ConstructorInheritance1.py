class A:

    def __init__(self):
        print("in A init")

    def feature(self):
        print("Feature 1 working")


class B(A):

    def feature2(self):
        print("Feature 2 working")


b = B()