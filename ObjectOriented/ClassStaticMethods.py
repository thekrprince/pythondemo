class School:

    school = "SXS"

    def __init__(self, math, sci, eng):
        self.m = math
        self.s = sci
        self.e = eng

    def avg(self):
        return (self.m + self.s + self.e)/3

    @classmethod
    def sch(cls):
        return cls.school

    @staticmethod
    def info():
        print("School is certified")


S1 = School(80, 68, 78)
S2 = School(58, 88, 82)

print(S1.avg())
print(School.sch())

School.info()