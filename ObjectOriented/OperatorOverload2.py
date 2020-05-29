class Greater:

    def __init__(self, val):
        self.a = val

    def __gt__(self, other):
        if self.a > other.a:
            return True
        else:
            return False


a1 = Greater(56)
a2 = Greater(78)

if a1 > a2:
    print("a1 wins")
else:
    print("a2 wins")