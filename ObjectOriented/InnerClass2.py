class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'VAIO'
            self.ram = 8

        def show(self):
            print(self.brand, self.ram)


S1 = Student('Prince', 19)
S1.show()

lapy = Student.Laptop()
lapy.show()