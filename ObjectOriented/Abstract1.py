from abc import ABC, abstractmethod

class Polygon(ABC):

    def noofsides(self):
        pass


class Hexagon(Polygon):

    def noofsides(self):
        print("Hexagon has six sides")


class Quadrilateral(Polygon):

    def noofsides(self):
        print("Quadrilateral has four sides")


class Triangle(Polygon):

    def noofsides(self):
        print("Triangle has 3 sides")


H = Hexagon()
H.noofsides()

Q = Quadrilateral()
Q.noofsides()

T = Triangle()
T.noofsides()