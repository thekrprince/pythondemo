class Student:

    def sum(self, a = None, b = None, c = None):
        res = 0
        if a != None and b != None and c != None:
            res = a + b + c
            return res
        elif a!=None and b!=None:
            res = a + b
            return res
        else:
            res = a
            return res


S = Student()
print(S.sum(3, 6, 5))
print(S.sum(8, 3))
print(S.sum(26))
