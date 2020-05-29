class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class Jupyter:

    def execute(self):
        print("Can write Machine Learning code")
        print("Has so many in-built libraries")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


id = Jupyter()
lap = Laptop()
lap.code(id)