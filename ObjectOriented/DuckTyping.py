class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


id = Pycharm()
lap = Laptop()
lap.code(id)
