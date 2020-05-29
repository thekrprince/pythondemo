class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lapy = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lapy.show()

    class Laptop:

        def __init__(self):
            self.brand = 'VAIO'
            self.ram = 8

        def show(self):
            print(self.brand, self.ram)


s1 = Student("Prince", 19)
s1.show()