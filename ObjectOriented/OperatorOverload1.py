class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


S1 = Student(68, 75)
S2 = Student(55, 94)

s3 = S1 + S2
print(s3.m1)
print(s3.m2)