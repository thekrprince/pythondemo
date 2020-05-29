class Sum:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a<=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

s = Sum()
itr = iter(s)

for ele in itr:
    print(ele)