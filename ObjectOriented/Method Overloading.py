class Avg:

    def add(self, a, b):
        sum = a + b
        return sum

    def add(self, a, b, c):
        sum = a + b + c
        return sum


avg = Avg()
print(avg.add(10,20))