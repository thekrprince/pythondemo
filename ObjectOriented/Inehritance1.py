class Animal:

    def eat(self):
        print("Animals have four feet")


class Tiger(Animal):

    def speak(self):
        print("Tiger roars")


t = Tiger()
t.speak()
t.eat()