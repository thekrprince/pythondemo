class Person:

    def __init__(self):
        self.name = "Prince"
        self.age = 24

    def compare(self, others):
        if self.age == others.age:
            return True
        else:
            return False


P1 = Person()
P2 = Person()

if P1.compare(P2):
    print("They are same")
else:
    print("They are different")

P2.age = 30

if P1.compare(P2):
    print("They are same")
else:
    print("They are different")